# COVER PAGE
# ================================================================
# 2530090_MartinezReyesJoseAlejandro
# Group: 103 or 1-1
# ================================================================


# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# Control structures in Python like if, for, and while help the
# program make decisions and repeat tasks. They are used to solve
# simple problems such as checking data, doing calculations,
# controlling logins, showing menus, and creating patterns.
# This file contains six exercises using these ideas.
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
# 7.1 PROBLEM 1: Total sum and even numbers sum
# ================================================================
# Description:
# This program calculates the total sum from 1 to N and also
# calculates the sum of only the even numbers.
#
# Inputs:
# - user_number (int)
#
# Outputs:
# - Total sum
# - Even sum
#
# Validations:
# - Must be a valid integer
# - Must be greater than 1
# ================================================================
"""
try:
    user_number = int(input("Enter a number: "))
except:
    user_number = 0

total_sum = 0
even_sum = 0

if user_number > 1:
    for num in range(1, user_number + 1):
        total_sum += num
        if num % 2 == 0:
            even_sum += num

if total_sum == 0:
    print("Error: invalid input")
else:
    print("Total sum:", total_sum)
    print("Even sum:", even_sum)
"""



# ================================================================
# 7.2 PROBLEM 2: Multiplication table
# ================================================================
# Description:
# This program prints the multiplication table of a base number.
#
# Inputs:
# - base_value (int)
# - max_limit (int)
#
# Outputs:
# - Multiplication results
#
# Validations:
# - Both values must be valid integers
# - Limit must be positive
# ================================================================
"""
try:
    base_value = int(input("Enter base number: "))
    max_limit = int(input("Enter limit: "))
except:
    max_limit = 0

multiplier = 1

if max_limit > 0:
    for _ in range(max_limit):
        table_result = base_value * multiplier
        print(f"{base_value} x {multiplier} = {table_result}")
        multiplier += 1
else:
    print("Error: invalid input")
"""



# ================================================================
# 7.3 PROBLEM 3: Average of numbers
# ================================================================
# Description:
# This program stores several numbers and calculates the average.
# The process finishes when the user enters 0.
#
# Inputs:
# - Values (float)
#
# Outputs:
# - Average
# - Quantity of values
# ================================================================
"""
numbers_list = []
finish_flag = False

while not finish_flag:
    user_input = input("Enter a number: ")

    if user_input == "0":
        finish_flag = True
    else:
        try:
            numbers_list.append(float(user_input))
        except:
            print("Error: Invalid number")

total_values = len(numbers_list)
sum_values = 0

if total_values == 0:
    print("Error: No data entered")
else:
    for value in numbers_list:
        sum_values += value

    average_value = sum_values / total_values
    print("Average:", average_value)
    print("Quantity of numbers:", total_values)
"""



# ================================================================
# 7.4 PROBLEM 4: Password validation with attempts
# ================================================================
# Description:
# This program allows only three attempts to enter the password.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - Login status
# ================================================================
"""
main_password = "admin123"
attempts = 0

while attempts < 3:
    entered_password = input("Enter your password: ")

    if attempts == 1:
        print("Warning: last attempt")

    if entered_password == main_password:
        print("Login successful")
        break
    else:
        print("Incorrect password")

    attempts += 1

if attempts >= 3:
    print("Too many attempts: Account locked")
"""



# ================================================================
# 7.5 PROBLEM 5: Menu with counter
# ================================================================
# Description:
# This program displays a menu and allows the user to interact
# with a counter.
#
# Inputs:
# - Menu option (int)
#
# Outputs:
# - Messages and current counter value
# ================================================================
"""
menu_option = 1
count_value = 0

while True:
    print("Menu:\
\n1: Show greeting\
\n2: Show counter value\
\n3: Increase counter\
\n0: Exit")

    menu_option = input("Select an option: ")

    try:
        menu_option = int(menu_option)
    except:
        menu_option = -1

    if menu_option == 1:
        print("HELLO!!")
    elif menu_option == 2:
        print("Current counter:", count_value)
    elif menu_option == 3:
        count_value += 1
    elif menu_option == 0:
        print("Good bye!!")
        break
    else:
        print("Error: invalid option")
"""



# ================================================================
# 7.6 PROBLEM 6: Star pyramid
# ================================================================
# Description:
# This program prints a star pyramid pattern based on the size.
#
# Inputs:
# - pyramid_size (int)
#
# Outputs:
# - Star pattern
# ================================================================
"""
try:
    pyramid_size = int(input("Enter the size: "))
except:
    print("Error: Invalid input")
    pyramid_size = 0

if pyramid_size > 0:
    for level in range(1, pyramid_size + 1):
        print("*" * level)

    for level in range(pyramid_size, 0, -1):
        print("*" * level)
else:
    print("Error: Invalid input")
"""



# ================================================================
# CONCLUSIONS
# ================================================================
# Control structures help a program decide what to do and repeat
# actions when needed. Using if, for, and while makes it possible
# to solve everyday problems like checking data, showing menus,
# and creating patterns. Validating input helps the program avoid
# errors and work correctly.
# ================================================================


# ================================================================
# REFERENCES
# ================================================================
# 1) Python Documentation - Control Flow
# 2) W3Schools - Python Loops and Conditions
# 3) RealPython - Input Validation in Python
# 4) Class Notes – Control Structures
# ================================================================