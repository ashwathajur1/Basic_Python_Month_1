# while condition:
#     # code block

count = 1

while count <= 5:
    print(count)        # prints 1 2 3 4 5 
    count = count + 1

# The below code runs forever if we dont keep condition(count = count + 1)
# while count <= 5:
#     print(count)

num = 1

while num != 0:
    num = int(input("Enter number (0 to stop): "))
    print("You entered:", num)    # Stops only when user enters 0.

# What if user types pqr instead of number? so coverting input value "pqr" to int is not possible our code throws error. To hand this we
# keep exception handling with try and except block as well as if condition to break while loop. Below is our improved code.
while True:
    try:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        print("You entered:", num)
    except ValueError:
        print("Invalid input. Enter a number.")


# Break: Stops loop immediately.
while True:
    x = int(input("Enter number: "))
    if x == 0:
        break
    print("Number:", x)


# Continue
# Skips current iteration.
i = 0
while i<5:
    i = i + 1
    if i==3:
        continue
    print(i)

# For loop
for i in range(1, 6):
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)


range(5)        # 0 to 4
range(1, 6)     # 1 to 5
range(1, 10, 2) # 1,3,5,7,9

for i in range(1,6,2):  #range function takes 3 inputs. 1st - start, 2nd - stop, 3rd - step
    if i == 3:
        continue
    print(i)


for i in range(5, 0, -1):
    print(i)



name = "Ash"
for char in name:  # Loops character by character.
    print(char)

# Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Task 1 — Print 1 to 50
# Using:
# while
# for

# Using while loop
i = 1
while i<=50:
    print(i)
    i = i + 1

# Using for loop
for i in range(1,51):
    print(i)


# Task 2 — Sum of First N Numbers
# Ask user for number N.
# Print sum of 1 to N.
# Edge case:
# If N negative?

n = abs(int(input("Enter a number: "))) # This works even if n is negative.
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)


# Task 3 — Multiplication Table
# Ask user for number.
# Print table up to 10.


n = int(input("Enter a number to print multiplication table: "))
for i in range(1,11):
    print(n,"*",i,"=",n * i)


# Task 4 — Count Digits
# Ask user for number.
# Count how many digits it has.
# (Hint: use while loop and // 10)
count = 0
rem = 0
n = int(input("Enter an integer to get number of digits in it: "))
while n!=0:
    if n % 10 > 0:
        count = count + 1
    n = n // 10
print(count)


# Task 5 — Prime Check (Logic Challenge)
# Ask user for number.
# Check if number is prime or not.
# (Hint: loop from 2 to n-1)
# Edge case:
# 0, 1, negative numbers.

import time
start = time.perf_counter()   
n = int(input("Enter an integer to check if prime or not: "))
if n < 2:
    print(n, "is not prime")
for i in range(2,n//2):
    if n%i==0:
        print(n, "is not a prime which is divisible by", i)
        break
if i == (n//2)-1:
    print(n, "is prime")
end = time.perf_counter()
print("Time taken:", end - start, "seconds")

