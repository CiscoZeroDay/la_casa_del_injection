from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os, subprocess, sqlite3, re

app = Flask(__name__)

# ---------------------------
# init DB SQLite vulnérable (simple)
# ---------------------------
DB_FILE = "users.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username,password) VALUES ('berlin','berlin123')")
    c.execute("INSERT INTO users (username,password) VALUES ('tokyo','tokyo123')")
    conn.commit()
    conn.close()

# ---------------------------
# secret file
# ---------------------------
SECRET_DIR = "/app/secret"
os.makedirs(SECRET_DIR, exist_ok=True)
with open(os.path.join(SECRET_DIR, "bankofspain.txt"), "w", encoding="utf-8") as f:
    f.write("You think that it's so easy !\n")

# ---------------------------
# routes
# ---------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portal", methods=["GET", "POST"])
def portal():
    msg = ""
    if request.method == "POST":
        u = request.form.get("username", "")
        p = request.form.get("password", "")
        # ⚠️ Vulnérable à la SQLi (concat directe). Payload: ' or 1=1 --
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        try:
            sql = f"SELECT * FROM users WHERE username='{u}' AND password='{p}' LIMIT 1"
            c.execute(sql)
            res = c.fetchone()
            if res:
                return redirect(url_for("central"))
            else:
                msg = "Identifiants invalides"
        except Exception as e:
            msg = str(e)
        finally:
            conn.close()
    return render_template("login.html", msg=msg)

@app.route("/portal/central")
def central():
    cmd = request.args.get("cmd", "")
    output, err = "", ""
    if cmd:
        # Interdit: cat/more/tail/head (doit utiliser less)
        if re.search(r"\b(cat|more|tail|head)\b", cmd, re.IGNORECASE):
            err = "Cette commande est interdite ici."
        else:
            try:
                output = subprocess.getoutput(cmd)
            except Exception as e:
                err = str(e)
    return render_template("central.html", output=output, err=err)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
