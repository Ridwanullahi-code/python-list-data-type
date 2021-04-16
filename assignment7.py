"""
Design a program that uses a main function to import 7 random numbers in the
range 0 to 9 assigns them to a list in a single line.
"""
from random import randint

def main():
	numbers_list = []
	for num in range(7):
		numbers = randint(0,10)
		numbers_list = + numbers
		print(numbers_list, end = "\t")

print(main())
