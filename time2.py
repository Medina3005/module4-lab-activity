# time2.py
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program asks the user for the current time and a wait time, then calculates the time the alarm will go off.

# Get user input for current time and wait time
str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert input to integers
time = int(str_time)
wait_time = int(str_wait_time)

# Calculate time when the alarm will go off
time_when_alarm_go_off = (time + wait_time) % 24

# Print result
print(f"The alarm will go off at {time_when_alarm_go_off}:00")


# Errors:
# Misspelled variable (wai_time → wait_time).
# Added modulus operation (% 24) to ensure time remains within 24-hour format.
# Improved user input prompt for clarity.
