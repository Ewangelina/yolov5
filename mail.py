import smtplib

already_sent = False
sender = 'projekt.test17@gmail.com'
password = 'armflaxmppnjnggx'
recipient = None

def send_email(subject, body):
    global already_sent
    if (already_sent):
        return
  
    message = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message)
        print("E-mail został wysłany!")
        already_sent = True
        server.quit()
    except Exception as e:
        print("Wystąpił błąd podczas wysyłania e-maila: ", str(e))

def set_recipient(new_recipient):
    global recipient, already_sent
    
    if new_recipient == None:
        already_sent = True
    else:
        recipient = new_recipient
