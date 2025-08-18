FROM ubuntu:22.04

# Installer dépendances
RUN apt-get update && apt-get install -y \
    python3 python3-pip vsftpd less\
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire nécessaire pour secure_chroot_dir
RUN mkdir -p /var/run/vsftpd/empty \
    && chown root:root /var/run/vsftpd/empty \
    && chmod 755 /var/run/vsftpd/empty

# Installer Flask
RUN pip3 install flask

# Créer utilisateur FTP
RUN useradd -m professor && echo "professor:graciastokyo" | chpasswd

# Config vsftpd minimal
RUN echo "listen=YES\n\
listen_ipv6=NO\n\
anonymous_enable=NO\n\
local_enable=YES\n\
write_enable=YES\n\
local_umask=022\n\
chroot_local_user=YES\n\
allow_writeable_chroot=YES\n\
pasv_enable=YES\n\
pasv_min_port=21100\n\
pasv_max_port=21110\n\
secure_chroot_dir=/var/run/vsftpd/empty\n\
" > /etc/vsftpd.conf

# Copier ton app Flask
WORKDIR /app
COPY ./web /app

# Copier fichiers FTP
COPY ./ftp_data /home/professor/
RUN chown -R professor:professor /home/professor/

# Script de démarrage
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Créer le dossier parent dans Flask
RUN mkdir -p /app/professor

# Copier document2.txt dans le dossier parent
COPY document2.txt /app/professor/document2.txt


# Exposer ports
EXPOSE 5000 21 21100-21110

CMD ["/start.sh"]
