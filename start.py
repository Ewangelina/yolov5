import action
import statistics
import mail
import detect

import os

while True:
	actions = input("Podaj numerał wybranego profilu akcji\n")
	try:
		if int(actions) >= 0:
			actions = int(actions)
			break
		else:
			print("Podaj poprawny numerał")
	except Exception as e:
        	print("Podaj poprawny numerał")

if actions % 5 == 0:
	email = input("Podaj adres e-mail\n")
	mail.set_recipient(email)

	
statistics.init_statistics()
action.set_option(actions)

print("Program starting, please wait")
detect.start()
