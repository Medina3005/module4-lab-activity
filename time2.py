str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time) % 24
print(f"The alarm will go off at {time_when_alarm_go_off}:00")


# Errors:
# Misspelled variable (wai_time → wait_time).
# Added modulus operation (% 24) to ensure time remains within 24-hour format.
# Improved user input prompt for clarity.