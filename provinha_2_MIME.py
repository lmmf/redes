import os
from flask import Flask
from flask import request


app = Flask(__name__)
def html():
	return '''<html>\n
<head><title>EMAIL</title></head>\n
<body>\n
  <h2>EMAIL</h2>\n
  <form method="get" action="/bin/login">\n
    Email: <input type="text" name="user" size="25" /><br /><br />\n
    Assunto: <input type="text" name="sub" size="50" /><br /><br />\n  
    Conteudo: <input type="text" name="pw" size="100" /><br /><br />\n  
    <input type="submit" value="SEND" />\n
  </form>\n
</body>\n
</html>'''

@app.route("/")
def index():
    return html()

#importa modulos de email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import socket as s

#print(ip)
def mandaemail((email, assunto, content)):

	return "<h1>"+str(email, assunto, content)+"Sucesso!</hi>"
	# dados
	body = content
	sub = assunto
	mail_from = 'freddysampaio9@gmail.com'
	mail_to = email
	pwd = 'fantauva'


	# preeenchendo os dados
	msg = MIMEMultipart('related')
	msg['From'] = mail_from
	msg['To'] = mail_to
	msg['Subject'] = sub
	msg.attach(MIMEText(body, 'plain'))


	# envia email
	# importa biblioteca
	import smtplib
	# altorizacao e autenticacao
	smtp = smtplib.SMTP('smtp.gmail.com',587)
	smtp.ehlo()
	smtp.starttls()
	smtp.login(mail_from, pwd)
	smtp.sendmail(mail_from, mail_to, msg.as_string())
	smtp.quit()

def pegaemail(mensagem):
	email=mensagem.split("user=")[1].split("&sub=")[0]
	assunto=mensagem.split("&sub=")[1].split("&pw=")[0]
	conteudo=mensagem.split("&pw=")[1].split(" ")[0]
	email=email.replace("%40", "@")
	assunto=assunto.replace("+", " ")
	conteudo=conteudo.replace("+", " ")
	return (email, assunto, conteudo)

@app.route("/bin/<mensagem>")
def resposta(mensagem):
	print(request.url)
	return mandaemail(pegaemail(str(request.url)))
	#return "<h1>"+request.url+"Sucesso!</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
