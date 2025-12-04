# ================================================================
# COVER PAGE
# ================================================================
# 2530090_MartinezReyesJoseAlejandro
# Group: 103 / 1-1
# Subject: Programming
# Topic: Control Structures in Python
# ================================================================

# Control structures help the program make decisions and repeat
# actions automatically. With if, for, and while the program can
# validate data, repeat processes, show menus, and build patterns.
# These tools make programs useful, organized, and interactive.



# ================================================================
# PROBLEM 1: TOTAL SUM AND EVEN SUM
# ================================================================
"""
This program asks the user for a number and calculates:
- The total sum from 1 to that number
- The sum of only the even numbers

It uses:
- try/except for input validation
- a FOR loop for repetition
- IF statements for conditions
"""

try:
    number = int(input("Enter your number: "))
except Exception as err:
    number = 1

total_sum = 0
even_sum = 0

if number > 1:
    for i in range(1, number + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i

if total_sum == 0 and even_sum == 0:
    print("Error: invalid input")
else:
    print(total_sum)
    print(even_sum)



# ================================================================
# PROBLEM 2: MULTIPLICATION TABLE
# ================================================================
"""
This program prints the multiplication table of a base number
up to a given limit using a FOR loop.
"""

try:
    base = int(input("Enter the base: "))
    m = int(input("Enter the limit: "))
except Exception as err:
    m = 1

result = 0
contador = 0

if m > 1:
    for multiplication_table in range(m):
        contador += 1
        resultado = base * contador
        print(f"{base} x {contador}= {resultado}")
else:
    print("Error: invalid input")



# ================================================================
# PROBLEM 3: AVERAGE OF NUMBERS
# ================================================================
"""
This program asks for numbers repeatedly using a WHILE loop.
When the user enters 0, it stops and calculates the average.
"""

numbers = []
end = None

while end != "0":
    new_number = input("Enter an number")
    try:
        numbers.append(float(new_number))
    except Exception as err:
        print("Error: Invalid input")

    end = input("If you do not wish to add another number, enter 0: ")

counter = 0
count = len(numbers)

if count == 0:
    print("Error: No data")
else:
    for number_suma in range(count):
        sumatoria = numbers[counter] + numbers[counter + 1]

    average = sumatoria / count
    print(f"Average: {average}")
    print(f"Quantity of numbers: {count}")



# ================================================================
# PROBLEM 4: PASSWORD ATTEMPTS
# ================================================================
"""
This program allows the user only three attempts to enter
the correct password using a WHILE loop.
"""

correct_password = "admin123"
counter = 0

while counter < 3:
    password = input("Enter your password: ")

    if counter == 1:
        print("Last attempt")
    elif correct_password == password:
        print("Login succes")
        break
    else:
        print("try again")

    counter += 1

if counter > 3:
    print("too many attempts: Account locked")



# ================================================================
# PROBLEM 5: MENU WITH COUNTER
# ================================================================
"""
This program shows a menu that lets the user:
- See a greeting
- See the counter
- Increase the counter
- Exit the program

It uses a WHILE TRUE loop and IF conditions.
"""

option = 1
counter_value = 0

while True:
    print("Menu:\
\n1:Show greeting\
\n2: Show current counter value\
\n3: Increment counter\
\n0: Exit")

    option = input("choice your option: ")

    try:
        option = int(option)
    except Exception as err:
        option = 4

    if option > -1 and option < 4:
        if option == 1:
            print("HELLO!!")
        elif option == 2:
            print(f"Thse current counter is: {counter_value}")
        elif option == 3:
            counter_value += 1
        elif option == 0:
            print("Good bye!!")
            break
    else:
        print("Error invalid option")



# ================================================================
# PROBLEM 6: STAR PYRAMID
# ================================================================
"""
This program prints a pyramid of stars using FOR loops.
One loop builds the pyramid up and the other builds it down.
"""

try:
    quantity = int(input("Enter the quantity: "))
except Exception as err:
    print("Error: Invalid imput")

for amount in range(1, quantity + 1):
    piramid = "*" * amount
    print(piramid)

for amount in range(quantity, 0, -1):
    inverted_piramid = "*" * amount
    print(inverted_piramid)



# ================================================================
# FINAL BASIC EXPLANATION
# ================================================================
"""
IF is used to make choices in the program.
FOR is used to repeat actions a specific number of times.
WHILE is used to repeat actions while a condition is true.

These control structures allow the program to work with user input,
repeat processes, show menus, and build patterns.
"""



# ================================================================
# REFERENCES
# ================================================================
"""
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/python_while_loops.asp
https://docs.python.org/3/tutorial/controlflow.html
"""
