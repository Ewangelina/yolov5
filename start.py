import action
import statistics
import mail
import detect

import os

while True:
	actions = input("Input selected action profile numeral\n")
	if int(actions) >= 0:
		actions = int(actions)
		break
	else:
		print("Please try again")

if actions % 5 == 0:
	email = input("Input the e-mail address the e-mail will be delivered to\n")
	mail.set_recipient(email)

	
statistics.init_statistics()
action.set_option(actions)

print("Program starting, please wait")
detect.start()
