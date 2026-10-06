"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Su
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
amount= int(input("How much do you want to save every month?"))
print("Please enter a whole number")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
total = amount * 12
# print this out for the user with a suitable message.
print("You will have saved £ ,total , by the end of the year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.

final_amount = total * 1.008
# print this out in the format £X.XX (to two decimal places).
print(f"With interest, you will have £",final_amount)