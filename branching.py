# branching.py
# by Medina Kubanychbekova
# Date: 02/12/2025
#Description: A time traveler program that categorizes the user into past, present, or future based on their year of origin.

# Ask user for their year of origin
year = int(input("Greetings! What is your year of origin? "))

# Determine the time period based on the input year
if year < 1900:
    print("Woah, that's the past!")
elif 1900 <= year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")

# Incorrect syntax in year assignment (== → =).
# Incorrect syntax in input() function call (int.input() → int(input())).
# Missing colon (:) in if and elif.
# Incorrect && operator in Python (&& → and).
# Fixed final elif condition
