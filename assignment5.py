"""
Create a menu which will be generated every time the user restarts the program
Tthis menu will also be shown after the output for each option .
The menu should be coded in a function named menu.Your menu should allow user to choose between the available options
accepting only  valid choice which stores the value choosen by the user.

CORRECT IMPLEMENTED PROGRAM
Choose your option below:
1- patient Registration
2- Total patient
3- Total sales
Q/q- Quit
your choice:5
invalid choice: please select from the list of choices.
"""

def menu():

	print("1- Patient Registration")
	print("2- Total Patient")
	print("3- Total sales")
	print("Q/q- Quit")

	loop = True
	while loop:

		option = print(input("Choose the option above: "))

		if option == 1:
			print("Patient Registration")

		elif option == 2:
			print("valid choice")

		elif option == 3:
			print("Total sales")

		elif option == "Q" or "q":
			loop = False

		else:
			print("invalid choice: please select from the list of choice")

print(menu())	