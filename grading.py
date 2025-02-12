# Calculating Grades (ok, let me think about this one)
# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program calculates the average of three exam grades, assigns a letter grade, and determines if the student is passing.

# Get user input for exam grades
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Store grades in a list
grades = [exam_one, exam_two, exam_three]

# Calculate the total and average score
total = sum(grades)
avg = total / len(grades)

# Determine the letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print each exam grade
for grade in grades:
    print(f"Exam: {grade}")

# Print final results
print(f"Average: {avg:.2f}")
print(f"Grade: {letter_grade}")

# Determine pass/fail status
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")



# Errors:
    
# Missing/misplaced parentheses in input().
# Incorrect string-to-integer conversion.
# Incorrect variable names (grdes → grades, grade → grades).
# Syntax errors in elif statements (: missing).
# Logical issue in grade calculation (letter_grade for D should be >= 60).
# Syntax errors in print statements.
