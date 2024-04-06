import datetime
def nhapyn (prompt):
	while True: #vong lap vo han 
		tl = input(prompt)
		if (tl == "yes") or (tl == "y") or (tl == "ok"):
			return True
		elif (tl == "no") or (tl == "not'") or (tl == "never"):
			return False
		else:
			continue
def tuoi (year_born):
	now = datetime.datetime.now()
	today = now.year
	return today - year_born

def meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = METER_TO_FEET * meter
	return feet

def print_infor(tall,full_name,bb,old):


	print("\n-----------")	

	print("FullName:" + full_name)
	print("You Age:" + str(old))
	print("Your Tall:" + str('%.1f' %tall) + " feet")

	if bb is True:
		print("You from vietnamese.")
	else:
		print("You not from Vietnamese.")

def tall_infor(tall,aa):
	a = 0
	if aa is True:
		if tall > 6.5:
			print("Super Tall Man",end =" ")
			for i in range(5):
				print("Very", end =" ")
		elif tall <6.0:
			print("Super Hero")
		else:
			print("You Short")
	elif aa is False:
		if tall > 5.8:
			print("Super Tall Gird")
		elif tall >5.5 and tall <= 5.8:
			print("Super gird")
		elif tall <5.0:
			print("Super short",end=" ")
			while a < 6:
				print("very" , end = " ")
				a += 1
	else:
		print("You Short ")

def main():
	fist_name = input("FistName:")
	last_name = input("LastName:")
	full_name = str(fist_name) + " " +  str(last_name)

	year_born = int(input("Year Born:"))
	old = tuoi(year_born)

	your_tall = float(input("Your Tall:"))
	tall = meter_to_feet(your_tall)#your_tall = meter

	aa = nhapyn("Are you Male(yes/no):")
	bb = nhapyn("Are you Vietnamese (yes/no):")

	print_infor(tall,full_name,bb,old)

	tall_infor(tall,aa)

main()