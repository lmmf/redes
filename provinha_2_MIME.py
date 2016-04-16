import os
from flask import Flask
from flask import request
from flask.ext.mail import Mail, Message


app = Flask(__name__)

app.config.update(dict(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='aspmx.l.google.com',
	MAIL_PORT=25,
	MAIL_USE_SSL=True,
	MAIL_USE_TLS=False,
	MAIL_USERNAME = 'freddysampaio9@gmail.com',
	MAIL_PASSWORD = 'fantauva'
	))


mail=Mail(app)

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


def pegaemail(mensagem):
	email=mensagem.split("user=")[1].split("&sub=")[0]
	assunto=mensagem.split("&sub=")[1].split("&pw=")[0]
	conteudo=mensagem.split("&pw=")[1].split(" ")[0]
	email=email.replace("%40", "@")
	assunto=assunto.replace("+", " ")
	conteudo=conteudo.replace("+", " ")
	return (email, assunto, conteudo)

@app.route("/bin/login")
def resposta():
	(email, assunto, conteudo)=pegaemail(str(request.url))	
	msg=Message(assunto, sender='freddysampaio9@gmail.com', recipients=[email])
	msg.body=conteudo
	mail.send(msg)
	print("\n\nTESTE\n\n")
	return "<h1>Sucesso!</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
