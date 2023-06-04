import action
import statistics
import mail
import detect

import os

def from_file():
	try:
		f = open("values.txt")
		actions = f.readline()
		if int(actions) >= 0:
			actions = int(actions)
			if actions % 5 == 0:
				email = f.readline()
				mail.set_recipient(email)
			
			statistics.init_statistics()
			action.set_option(actions)
			f.close()
			print("Program starting, please wait")
			detect.start()
		else:
			print("ERROR in values file")
	except:
		print("ERROR in values file")
		
def from_user(actions):
	while True:
		try:
			if int(actions) >= 0:
				actions = int(actions)
				break
			else:
				print("Incorrect action numeral inputed")
				actions = input("Input the selected action profile numeral: \n")
		except:
			print("Incorrect action numeral inputed")
			actions = input("Input the selected action profile numeral: \n")
	
	if actions % 5 == 0:
		email = input("Input e-mail address:\n")
		mail.set_recipient(email)

	statistics.init_statistics()
	action.set_option(actions)

	print("Program starting, please wait")
	detect.start()

actions = input("Input the selected action profile numeral: \n")
if actions == "":
	from_file()
else:
	from_user(actions)
