#!/bin/bash

# Lancer vsftpd en arrière-plan
/usr/sbin/vsftpd /etc/vsftpd.conf &

# Lancer Flask
python3 /app/app.py
