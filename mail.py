#E-mail adress the mesage will be sent to
recipient = "235842@edu.p.lodz.pl"


import smtplib

already_sent = False

def send_email(subject, body):
    global already_sent
    if (already_sent):
        return

    sender = 'projekt.test17@gmail.com'
    password = 'armflaxmppnjnggx'
    message = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message)
        print("The e-mail was succesfully sent!")
        already_sent = True
        server.quit()
    except Exception as e:
        print("The following error ocurred whilst sending the e-mail: ", str(e))
