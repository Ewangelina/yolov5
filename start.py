import action
import statistics
import mail
import detect

import os

while True:
	actions = input("Input the selected action profile numeral: \n")
	try:
		if int(actions) >= 0:
			actions = int(actions)
			break
		else:
			print("Incorrect action numeral inputed")
	except Exception as e:
        	print("Incorrect action numeral inputed")

if actions % 5 == 0:
	email = input("Input e-mail address:\n")
	mail.set_recipient(email)

	
statistics.init_statistics()
action.set_option(actions)

print("Program starting, please wait")
detect.start()
