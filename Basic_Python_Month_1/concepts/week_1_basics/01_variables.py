# variables
name = "Ashwath" 
age = 17
height = 5.6
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


print(5 / 2)              # Divides and gives 2.5(float value)
print(5 // 2)             # Gives 2 (floor division -> Eliminates digits after decimal)
print(22/7)
print(22//7)

print(0.1 + 0.2)  # Why not exactly 0.3? --> Floating-point precision issue. This teaches: Computers store decimals in binary → not perfect.

print("Hello" + "World")  # Works
# print("Hello" + 5)        # ERROR --> Use print("Hello" + str(5))
print(1+2)


is_student = True
is_logged_in = False

print("print")
# print(abc) # Error becuase abc is not a variable or keyword or string.
print(type(print)) # Gives : <class 'builtin_function_or_method'>
print(type(True))
print(type(True))
print(5 > 3)     # Boolean result

print("---")
print(bool(True))    # True         
print(bool(False))   # False
print(bool(""))      # False # Except Empty string, False and 0, bool of every other data is True.
print(bool(" "))     # True  # In this bool function as got input a space character so it is True.
print(bool("Hi"))    # True
print(bool(0))       # False
print(bool(1))       # True


x = "5"
# print(x + 5)   # ERROR -- Becuase x has string value.

x = 4
print(x,type(x),"4",6) # By default, Python inserts a separator when we use comma in print

print(type(type(x)))  # Gives <class 'type'>
print(type(type(print)))  # Gives <class 'type'>

x =  " "
print(x, type(x)) 

x = ""  # Empty string
print(x, type(x))
print(f"(x){type(x)}") # Empty string never retruns anything.


age = "25"
age = int(age)
print(age,"    ",type(age))

print(int(1.7))   # Gives value 1 which if floor value of 1.7 or python just eliminates decimal part of the value. Type Conversion: Python knows how to "truncate" (cut off) the decimal part of a float to make it an integer.
print(int("10"))      # OK gives 10
# print(int("10.5"))    # ERROR --> Syntactic Strictness: A string with a . is not a valid integer literal. Python refuses to "guess" if you want to round or truncate.
# print(int("abc"))     # ERROR


# print(age2) # Error -> NameError

name = "John"
# print(Name)  # ERROR --> Variable name is case sensitive

# ===========================================================

# Task 1
# Create 4 variables:
# Your name
# Your age
# Your height
# Whether you are a CS student
# Print them with type().


name = "Ashwath"
age = 17
height = 5.6
is_student = True

print("Name is:", name, "and Type is:",type(name))
print("Age is:", age, "and Type is:",type(age))
print("Height is:", height, "and Type is:",type(height))
print("Is he a student?:", is_student, "and Type is:",type(is_student))

# Task 2
# Convert
# "50" → int
# "20.5" → float
# 100 → string
# 0 → boolean

a = "50"
a = int(a)
print("Type of",a,"is:",type(a))

a = "20.5"
a = float(a)
print("Type of:",a,"is:",type(a))

a = 100
a = str(a)
print("Type of:",a,"is:",type(a))

a = 0
a = bool(a)
print("Type of:",a,"is:",type(a))


# Task 3 (Edge Case Thinking)
# What happens?
a = 5
b = "5"
print(a == b) # Result is False

# Task 4
print(bool("False")) # Result is: True. Except Empty string, False and 0, bool of every other data is True.


# Just trying merge conflict scenario case with main branch
print("Concept-learning version")
print("Hello")
# Just trying merge confict scenario
print("Main branch version")
