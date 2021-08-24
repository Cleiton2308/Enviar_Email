"""
#Para rodar esse codigo e necessario:
habilitar no seu e-mail a opção Permitir aplicativos menos seguros:
que fica no menu segurança#
"""

import smtplib

sender = "seu_email@gmail.com"
receiver = "email_destinatario@gmail.com"
password = "Sua senha de E-mail"
subject = "Python email test"
body = "I wrote an email! :D"

message = f"""From: Snoop Dogg{sender}
To: Nicolas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
