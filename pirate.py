 pirate.py
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: A simple pirate-themed password checker.

# Ask user for a greeting (password)
greeting = input("Hello, possible pirate! What's the password? ")

# Check if the user is a pirate
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")

greeting = input("Hello, possible pirate! What's the password? ")

if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")


# Errors:
# Missing closing quote in input().
# Incorrect use of square brackets (["Arrr!"] → ["Arrr!"]).
# Syntax error in elif
