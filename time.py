# time.py
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program calculates and prints the future time after a given wait time.

# Get user input for current time and wait time
currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

# Convert input to integers
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Calculate future time (ensuring it wraps within 24-hour format)
finalTimeInt = (currentTimeInt + waitTimeInt) % 24

# Print the final time
print(f"The time after waiting will be: {finalTimeInt}:00")


# Errors:
# Missing closing parenthesis in input().
# Inconsistent variable names (current_time_str instead of currentTimeStr).
# Misspelled variable (finalTime_Int → finalTimeInt).
