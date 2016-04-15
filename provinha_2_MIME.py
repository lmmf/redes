import os
from flask import Flask
from flask import request
# importa biblioteca
import smtplib
#importa modulos de email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import socket as s


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



#print(ip)
def mandaemail(email, assunto, conteudo):
	# dados
	body = conteudo
	sub = assunto
	mail_from = 'provinharedes@outlook.com'
	mail_to = email
	pwd = 'Apenasumteste'


	# preeenchendo os dados
	msg = MIMEMultipart('related')
	msg['From'] = mail_from
	msg['To'] = mail_to
	msg['Subject'] = sub
	msg.attach(MIMEText(body, 'plain'))
	# envia email
	
	# altorizacao e autenticacao
	smtp = smtplib.SMTP('smtp-mail.outlook.com',587)
	smtp.ehlo()
	smtp.starttls()
	print("\n\nTESTE1\n\n")
	smtp.login(mail_from, pwd)
	print("\n\nTESTE2\n\n")
	smtp.sendmail(mail_from, mail_to, msg.as_string())
	smtp.quit()

def pegaemail(mensagem):
	email=mensagem.split("user=")[1].split("&sub=")[0]
	assunto=mensagem.split("&sub=")[1].split("&pw=")[0]
	conteudo=mensagem.split("&pw=")[1].split(" ")[0]
	email=email.replace("%40", "@")
	assunto=assunto.replace("+", " ")
	conteudo=conteudo.replace("+", " ")
	mandaemail(email, assunto, conteudo)

@app.route("/bin/login")
def resposta():
	pegaemail(str(request.url))
	return "<h1>Sucesso!</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
