import smtplib

already_sent = False

def send_email(subject, body, recipient):
    global already_sent
    if (already_sent):
        return

    sender = 'projekt.test17@gmail.com'
    password = ''
    message = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message)
        print("E-mail został wysłany!")
        already_sent = True
    except Exception as e:
        print("Wystąpił błąd podczas wysyłania e-maila:", str(e))
    finally:
        server.quit()
