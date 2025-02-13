import mail
import snippets
import statistics

from datetime import datetime

taking_action = False
option = 0

def set_option(new_option):
    global option
    option = new_option

def continue_action(frame):
    if option % 3 == 0: #make snippet
        snippets.make_snippet(frame)
    

def take_action(frame):
    global taking_action
    if (taking_action):
        continue_action(frame)
        return
    
    taking_action = True
    
    if option % 3 == 0: #make snippet
        snippets.make_snippet(frame)

    if option % 5 == 0: #send email
        now = datetime.now()
        body = now.strftime("%d.%m.%Y at %H:%M:%S") + " a motorcycle was detected"
        mail.send_email("Motorcycle detection", body)

def end_action():
    global taking_action
    if not taking_action:
        return
    
    taking_action = False
    if option % 3 == 0: #make snippet
        snippets.end_snippet()

    statistics.motorcycles_exited_action()
