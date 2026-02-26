age = 18

if age >= 18:
    print("You are an adult")

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Edge case
if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Adult")
else:
    print("Minor")


marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# What happens?
if marks >= 50:
    print("C")
elif marks >= 75:
    print("B")

# If marks = 80
# It prints C.
# Because first condition is already True.
# Python stops checking after first True.
# Always write from most strict → least strict.



age = int(input("Enter age: "))

citizen = input("Are you a citizen? (yes/no): ")

# Nested if condition concept
if age >= 18:
    if citizen == "yes":
        print("You can vote")
    else:
        print("Citizenship required")
else:
    print("Too young to vote")

# The above nested if condition can be written as below:
if age>=18 and citizen == "yes":
    print("You can vote")
elif age>=18 and citizen == "no":
    print("Citizen required")
else:
    print("Too young to vote")


# Edge Case Thinking
# What if user enters:
# Yes
# YES
# yEs
# String comparison fails because "YES" is not equal to "yes". So keep
# if citizen.lower() == "yes":
# Now it handles case variations.


age = int(input("Enter age: "))
salary = int(input("Enter salary: "))

if age >= 21 and salary >= 20000:
    print("Loan approved")
else:
    print("Loan rejected")


# Exception handling
try:
    age = int(input("Enter age: "))
    if age < 0:
        print("Invalid input")
    elif age >= 18:
        print("Adult")
    else:
        print("Minor")
except ValueError:
    print("Please enter a valid number.")


# Task 1 — Even or Odd
# Ask user for number.
# If invalid → show error.
# If valid → check even or odd.

num1 = int(input("Enter the 1st num: "))
if num1%2==0:
    print(num1,"is even")
else:
    print(num1,"is odd")


# Task 2 — Largest of Three Numbers
# Ask user for 3 numbers.
# Find largest using only if/elif/else.
# Edge case:
# What if two numbers are equal?

num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))
num3 = int(input("Enter the third num: "))

if num1>num2 and num1>num3:
    print(num1, "is greater than", num2, "and", num3)
elif num2>num3:
    print(num2, "is greater than", num1, "and", num3)
else:
    print(num3, "is greater than", num2, "and", num1)
# For edge case this works well.


# Task 3 — Password Checker (Basic)
# Ask user to enter password.
# Rules:
# At least 8 characters
# Must contain a number
# Hint: Use: any(char.isdigit() for char in password)

password = input("Enter a valid password: ")
count = len(password)
if count >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is invalid")


# Task 4 — Number Category
# Ask user for number.
# Print:
# Positive even
# Positive odd
# Negative even
# Negative odd
# Zero

num = int(input("Enter a number: "))
if num > 0:
    if num%2==0:
        print(num,"is positive even")
    else:
        print(num,"is positive odd")
elif num<0:
    if num%2==0:
        print(num, "is negative even")
    else:
        print(num,"is negative odd")
else:
    print(num, "is zero")


# Task 5 — Predict Output
x = 10

if x > 5:
    print("A")
if x > 8:
    print("B")
else:
    print("C")



