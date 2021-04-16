print("Welcome to Covid 19 Test Center")

def PatientRegistration():
	totalPCR = 0
	totalAntigen = 0
	totalChild = 0
	totalSenior = 0
	Gender = "f" or "m"
	count = 1

	print("Please input your details below:")
	print("1: PCR  2:Antigen test " )
	while count == 1:

		Name = input("Name: ")

		Age = int(input("Age: "))
		if Age == list(range(1,11)):
			totalChild += Age
			print(totalChild)

		elif Age > 60:
			totalSenior += Age
			print(totalSenior)

		Gender = input("Gender[F/M]: ")

		Type = int(input(" Type: [1/2]"))
		if Type == 1:
			totalPCR += Type
			print(totalPCR)

		elif Type == 2:
			totalAntigen += Type
			print(totalAntigen)

		print(f"Total Child: {totalChild} ")
		print(f"total Senior: {totalSenior}")
		print(f"total Antigen: {totalAntigen}")
		print(f"total PCR: {totalPCR}")

		
print(PatientRegistration())
