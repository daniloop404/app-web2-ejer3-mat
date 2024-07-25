import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    sender_email = os.environ['EMAIL_USER']
    sender_password = os.environ['EMAIL_PASS']

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python send_email.py <asunto> <mensaje> <correo_destinatario>")
    else:
        subject = sys.argv[1]
        body = sys.argv[2]
        to_email = sys.argv[3]
        send_email(subject, body, to_email)