## WRITEUP - LA CASA DE L'INJECTION.
- **Category**: Web
- **Level:** : Medium

**Description:** Le professeur est attrapé par la police d'Espagne, et il a besoin de toi pour trouver deux document sur leur système privé. Ces documens contient le flag qui va innocenter le Professor.
Tu vas travailler avec l'equipe de Casa del Papel pour ca.

----------------------------------------------------------------------
## Step 1 :  Download the docker image
-----------------------------------------

-  The docker images is available on my docker hub.

<pre>Link : https://hub.docker.com/repositories/razafindraibe</pre>

<pre>sudo docker pull razafindraibe/la_casa_de_injection:latest</pre>
![alt text](imagewriteup/1.png)

- Run the container :
<pre>sudo docker run -d -p 8080:5000 -p 21:21 -p 21100-21110:21100-21110 razafindraibe/la_casa_de_injection:latest</pre>

![alt text](imagewriteup/2.png)

---------------------------------------------------------------------
## Step 2 : Reconnaissance

**1 - Let’s start with a simple IP scan using :** nmap
![alt text](imagewriteup/3.png)

---------------------------------------------------------------------
**2 - Let's access the site :**

<pre>http://localhost:8080</pre>

![alt text](imagewriteup/4.png)

We accessed the blog of the group.

El Profesor sent a photo to **Berlin** before his arrest.

Hmmm... it seems to be about steganography.

---------------------------------------------------------------------
**3- Download the photo**

Just click on it and it will be downloaded.

- Hint : Pigpen Cipher

![alt text](imagewriteup/7.png)

Good job! We have credentials, either for FTP or for a login.

---------------------------------------------------------------------
**4 - Let's try to connect by ftp on port 21**

<pre>ftp 127.0.0.1</pre>

- username: professor
- password: graciastokyo

![alt text](imagewriteup/9.png)

<pre>get document1.txt</pre>

![alt text](imagewriteup/11.png)

Bravo !! We got the first document

![alt text](imagewriteup/30.jpg)

---------------------------------------------------------------------
## Step 3 : Search the second document !

**Let’s continue our exploration with gobuster**

![alt text](imagewriteup/8.png)
We have */portal* . It seems important.

![alt text](imagewriteup/14.png)

It's a login page

---------------------------------------------------------------------
## Step 4 : Injection

As the name of the challenge is **LA CASA DE L'INJECTION**, maybe the website is vulnerable to SQL injection.

![alt text](imagewriteup/16.png)

Boom!! It worked, and we accessed the **WEB SERVER COMMAND PANEL**

![alt text](imagewriteup/18.png)

**/secret** and **/professor** are interesting .

![alt text](imagewriteup/19.png)

![alt text](imagewriteup/20.png)

Unfortunately .. We can't use cat. Let's try with another one.

![alt text](imagewriteup/22.png)

Hummmmm... it's not the second document. Let's take a look on /professor

![alt text](imagewriteup/23.png)

Bingo !!!!

![alt text](imagewriteup/32.jpg)

We combined document1 and document2 contents, got the flag, and saved the Professor.


---------------------------------------------------------------------
