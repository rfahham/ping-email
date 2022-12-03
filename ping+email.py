# !/usr/bin/env python
# -- coding: utf-8 --

import os
import smtplib
import getpass
import threading 
from time import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Timer

cores = {'vermelho':'\033[31m','verde':'\033[32m',}
hostname = "globo.com"
response = os.system("ping -c 1 " + hostname)
# beep = os.system( "say Vamos testar !!!" )

def enviar_email():
	
	email = "rfahham@hotmail.com"
	# password = getpass.getpass('Digite sua senha: ')
	password = ""
	send_to_email = "rfahham@hotmail.com"
	subject = "Teste de conexão com o servidor"
	message = "O servidor parou de responder!"
		
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject
		
	msg.attach(MIMEText(message, 'html'))
	
	server = smtplib.SMTP('SMTP.office365.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()
	server.sendmail(email, send_to_email, text)
	server.quit()

def validar():
	if response == 0:
		print("")
		print('\033[32mServer is UP !!!\033[m ')
	else:
		enviar_email()
		print('\033[31mServer is DOWN !!!\033[m ')
		beep
	sleep(10)

while True:
	validar()

