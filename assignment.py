# base from the given list below create a python function using the following condition as specified below
# (a) create a seperated lists of string and numbers
# (b) sort the strings list in ascending order
# (c) sort the string list in descending order
# (d) sort the number list from the lowest to high
# (e) sort the number list from highest to lowest

gadget = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
		"Televison", 1000, "Laptop Case", "Camera Lens",
]
string_list = []
number_list = []

for string in gadget:
	if type(string) == str:
		string_list.append(string)

	else:
		number_list.append(string)

print("Question a answer")
print(string_list)
print(number_list)

print("Question b answer")
sort_string = sorted(string_list)
print(sort_string)
print("Question c answer")
print(sort_string[::-1])

print("Question d answer")
sort_number = sorted(number_list)
print(sort_number)
print("Question e answer")
print(sort_number[::-1])
