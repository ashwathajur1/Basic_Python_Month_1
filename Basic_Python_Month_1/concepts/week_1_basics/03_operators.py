a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3  (floor division)
print(a % b)   # 1  (remainder)
print(a ** b)  # 1000 (power)

"""
a = input("Enter an interger: ") # Input function takes string. For example: If user inputs 4 ,variable a will have "4".
b = input("Enter another integer: ") # "6"
c = a+b # Result is: "46" --> Becuase + operator concatenates both strings "4" and "6" from variable a and b.
print("Addition of",a,"and",b,"is:",c)

a = int(input("Enter an interger: ")) # Output of input function is string. We converted string to int format. "4" --> 4
b = int(input("Enter another integer: ")) # "6" --> 6
c = a+b # Result is: 10
print("Addition of",a,"and",b,"is:",c)

"""

# Test
# print(10 / 0)      # Error is ZeroDivisionError
# print(10 // 0)     # Error is ZeroDivisionError
# print(10 % 0)      # Error is ZeroDivisionError

# Comparison Operators
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= 5)
print(x <= 5)


x = 5
print(x == 5)  # Comparison
# print(x = 5)   # ERROR

# = → assignment
# == → comparison

print("5" == 5) # False. Because different types.

# Logical Operators
a = 10

print(a > 5 and a < 20)
print(a > 5 or a > 100)
print(not(a > 5))

print(False and 10/0) # and operator stops when first condition is False.

print(True or 10/0) # or operator stops when first condition is True.

print(2 + 3 * 4)
print((2 + 3) * 4)

x = 10
x += 5 # This is also equal to x = x + 5
x -= 3 # This is also equal to x = x - 5
x *= 2 # This is also equal to x = x * 5
x /= 4 # This is also equal to x = x / 5 

print(x)

# num = int(input("Enter number: "))

# if num != 0:
#     print(100 / num)
# else:
#     print("Cannot divide by zero")


# Practice Exercises
# Task 1
# Ask user for 2 numbers.
# Print:
# Which is greater
# If equal

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))


# if num1>num2:
#     print(num1,"is greater than",num2)
# elif num2>num1:
#     print(num2,"is greater than",num1)
# elif num1 == num2:
#     print(num1,"and",num2,"both are equal")


# Task 2

# Ask user for a number.
# Check if:
# Positive
# Negative
# Zero

# num1 = float(input("Enter 1st number: "))

# if num1>0:
#     print(num1,"is positive")
# elif num1<0:
#     print(num1,"is negative")
# else:
#     print(num1,"is equal to Zero")


# Task 3
# Ask user for a number.
# Check if: 
# Number is even

num1=int(input("Enter the first number: "))
if num1%2==0:
    print(num1,"is even")

else:
    print(num1,"is odd")


# Task 4
# Ask user for 3 numbers.
# Find largest using only comparison operators.
# (No built-in max() allowed.)

num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2st num: "))
num3 = int(input("Enter 3rd num: "))

if num1>num2 and num1>num3:
    print(num1,"is greater than",num2,"and",num3)
elif num2>num3: # Since in first if condition num1>num2 is not True so no need to check num2>num1 in this elif.
    print(num2,"is greater than",num1,"and",num3)
else:
    print(num3,"is greater than",num1,"and",num2)

print(True and False or True) # Result is True

x = 0
print(x != 0 and 10/x > 1) # False

# print(10/x > 1 and x != 0) # Error





