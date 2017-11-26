"""

Problem 1.

Write a program that asks the user for a number (integer only) and prints the sum of its digits

"""
input_number = input("Enter a number: ")
input_number_string = str(input_number)  # Convert number to string so as to iterate through the digits
list_digits = [int(digit) for digit in input_number_string]  # Create a list containing all digits
sum_digits = sum(list_digits)  # Sum the elements of the list
print sum_digits