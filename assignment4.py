# python group conversation
import re
print("welcome to facebook")
print("Meet Million of Friends here")

action = input("Do you want to open account? ")

if action == "yes":
	
	def name():

		user_surname = input("Input Your Surname: ")

		first_name = input("Input Your First Name: ")

		middle_name = input("Input Your Middle Name: ")

		print(user_surname, " " + first_name, " " + middle_name)

	def password():
		print("your password must be minimum of 8 characters")

		user_password = input("Input Your password: ")
		
		if len(user_password) < 8:

			print("Your password is incomplete")
			return input("Input Your password again: ")

		elif len(user_password) > 8:

			return (user_password)

	def email():
		user_email = input("Input Your Email: ")

		pattern = re.compile(r"\w+@[a-z]+\.[a-z]+")

		if pattern.search(user_email):

			return (user_email)

		else:
			print(input("Input Your email again: "))
			return (user_email)

	def age():

		user_age = input("Input Your Age: ")
		if user_age < 18:
			print("oh you are not eligible to open this site")
			return(input("Input Your Age Again: "))
		elif user_age > 18:
			print(user_age)
	
elif action == "no":

		print(email())
		print(password())


print(name())
print(password())
print(email())
print(age())
print(user_info())
