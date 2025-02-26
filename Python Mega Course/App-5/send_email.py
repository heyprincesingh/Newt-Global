import smtplib, ssl, os

from dotenv import load_dotenv                  # type: ignore

load_dotenv() 

def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 587  # TLS port

    username = os.getenv("email_username")
    password = os.getenv("email_password")
    
    receiver = user_email
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, receiver, message)
