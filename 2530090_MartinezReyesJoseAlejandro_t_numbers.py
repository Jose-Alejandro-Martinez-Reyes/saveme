# PORTADA
# ================================================================
#2530090_MartinezReyesJoseAlejandro
#  Grupo: 103 ó 1-1
# ================================================================


# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# Control structures in Python such as if, for, and while are used
# to make decisions and repeat actions. These structures are basic
# tools for solving programming problems such as validations,
# calculations, authentication systems, menus, and patterns.
# This document includes six exercises using these structures.
# ================================================================


# ================================================================
# PRINCIPLES AND BEST PRACTICES
# ================================================================
# - Validate all user input before processing.
# - Use try and except to avoid execution errors.
# - Use loops for repeated processes.
# - Use counters and accumulators correctly.
# - Keep logic simple and readable.
# ================================================================



# ================================================================
# 7.1 PROBLEM 1: Sum and even sum
# ================================================================
# Description:
# This program calculates the sum from 1 to N and the sum of even
# numbers only.
#
# Inputs:
# - number (int)
#
# Outputs:
# - Total sum
# - Even numbers sum
#
# Validations:
# - Must be a valid integer
# - Must be greater than 1
# ================================================================
"""
try:
    number = int(input("Enter a number: "))
except:
    number = 0

sum_total = 0
sum_even = 0

if number > 1:
    for value in range(1, number + 1):
        sum_total += value
        if value % 2 == 0:
            sum_even += value

if sum_total == 0:
    print("Error: invalid input")
else:
    print("Total:", sum_total)
    print("Even:", sum_even)
"""



# ================================================================
# 7.2 PROBLEM 2: Multiplication table
# ================================================================
# Description:
# This program prints the multiplication table for a base number.
#
# Inputs:
# - base (int)
# - limit (int)
#
# Outputs:
# - Multiplication results
#
# Validations:
# - Both must be valid integers
# - Limit must be positive
# ================================================================
"""
try:
    base = int(input("Enter base: "))
    limit = int(input("Enter limit: "))
except:
    limit = 0

count = 1

if limit > 0:
    for _ in range(limit):
        result = base * count
        print(f"{base} x {count} = {result}")
        count += 1
else:
    print("Error: invalid input")
"""



# ================================================================
# 7.3 PROBLEM 3: Average of numbers
# ================================================================
# Description:
# This program stores several numbers and calculates their average.
# The process ends when the user enters 0.
#
# Inputs:
# - Numbers (float)
#
# Outputs:
# - Average
# - Total quantity of numbers
# ================================================================
"""
data_list = []
stop = None

while stop != "0":
    value = input("Enter a number: ")
    if value == "0":
        break
    try:
        data_list.append(float(value))
    except:
        print("Error: Invalid input")

    stop = input("To finish, enter 0: ")

total_items = len(data_list)
total_sum = 0

if total_items == 0:
    print("Error: No data")
else:
    for item in data_list:
        total_sum += item

    average = total_sum / total_items
    print("Average:", average)
    print("Quantity of numbers:", total_items)
"""



# ================================================================
# 7.4 PROBLEM 4: Password attempts
# ================================================================
# Description:
# This program validates a password with only three attempts.
#
# Inputs:
# - password (string)
#
# Outputs:
# - Access result
# ================================================================
"""
correct_password = "admin123"
tries = 0

while tries < 3:
    user_password = input("Enter your password: ")

    if tries == 1:
        print("This is your last attempt")

    if user_password == correct_password:
        print("Login success")
        break
    else:
        print("Incorrect password")

    tries += 1

if tries >= 3:
    print("Too many attempts: Account locked")
"""



# ================================================================
# 7.5 PROBLEM 5: Menu with counter
# ================================================================
# Description:
# This program displays a menu with different options.
#
# Inputs:
# - Menu option
#
# Outputs:
# - Messages and counter value
# ================================================================
"""
option = 1
counter = 0

while True:
    print("Menu:\
\n1: Show greeting\
\n2: Show counter value\
\n3: Increase counter\
\n0: Exit")

    option = input("Select an option: ")

    try:
        option = int(option)
    except:
        option = 9

    if option == 1:
        print("HELLO!!")
    elif option == 2:
        print(f"Current counter: {counter}")
    elif option == 3:
        counter += 1
    elif option == 0:
        print("Good bye!!")
        break
    else:
        print("Error: invalid option")
"""



# ================================================================
# 7.6 PROBLEM 6: Star pyramid
# ================================================================
# Description:
# This program prints a pyramid made of stars.
#
# Inputs:
# - size (int)
#
# Outputs:
# - Pyramid pattern
# ================================================================
"""
try:
    size = int(input("Enter the size: "))
except:
    print("Error: Invalid input")
    size = 0

if size > 0:
    for i in range(1, size + 1):
        print("*" * i)

    for i in range(size, 0, -1):
        print("*" * i)
else:
    print("Error: Invalid input")
"""



# ================================================================
# CONCLUSIONS
# ================================================================
# Loops and conditional statements allow solving repetitive and
# logical problems efficiently. Input validation avoids runtime
# errors and ensures reliable results. These concepts are essential
# for basic programming development.
# ================================================================
