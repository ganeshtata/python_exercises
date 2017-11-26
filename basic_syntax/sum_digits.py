"""

Problem 1.

Write a program that asks the user for a number (integer only) and prints the sum of its digits

"""


def method1(input_number):
	"""
	Description : Finds sum of all digits in a number by converting the number to string, and iterating through each digit
	"""
	input_number_string = str(input_number)  # Convert number to string so as to iterate through the digits
	list_digits = [int(digit) for digit in input_number_string]  # Create a list containing all digits
	sum_digits = sum(list_digits)  # Sum the elements of the list
	return sum_digits


def method2(input_number):
	"""
	Description : Finds sum of all digits in a number,by summing over the unit digit of the number in each successive iteration, where the number is divided by 10 in every iteration
	"""
	sum_digits = 0
	while input_number != 0:
		sum_digits += input_number % 10
		input_number = input_number / 10
	return sum_digits

input_number = input("Enter a number: ")
print method1(input_number)
print method2(input_number)