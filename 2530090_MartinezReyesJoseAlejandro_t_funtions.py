"""
 COVER PAGE

 2530090_MartinezReyesJoseAlejandro
 Group: 103 / 1-1

"""

"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 1: RECTANGLE AREA AND PERIMETER
in this code i need to calculate the size of area and primetre

"""

def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

if width <= 0 or height <= 0:
    print("Invalid input")
else:
    print("Area:", rectangle_area(width, height))
    print("Perimeter:", rectangle_perimeter(width, height))


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 2: GRADE CLASSIFIER
This function receives a number and give an asociate grade

"""

def grade_category(score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    else:
        return "Grade F"


score = int(input("\nEnter your grade: "))
result = grade_category(score)
print(result)


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 3: LIST STATISTICS
This function receives a list of numbers
It returns the minimum, maximum and average

"""

def number_summary(numbers):
    minimum_value = min(numbers)
    maximum_value = max(numbers)
    average_value = sum(numbers) / len(numbers)

    return {
        "min": minimum_value,
        "max": maximum_value,
        "average": average_value
    }


numbers_text = input("\nEnter numbers separated by commas: ")

try:
    numbers_text = numbers_text.split(",")

    n1 = float(numbers_text[0])
    n2 = float(numbers_text[1])

    if len(numbers_text) == 2:
        numbers = [n1, n2]
    elif len(numbers_text) == 3:
        n3 = float(numbers_text[2])
        numbers = [n1, n2, n3]
    elif len(numbers_text) == 4:
        n3 = float(numbers_text[2])
        n4 = float(numbers_text[3])
        numbers = [n1, n2, n3, n4]
    else:
        n3 = float(numbers_text[2])
        n4 = float(numbers_text[3])
        n5 = float(numbers_text[4])
        numbers = [n1, n2, n3, n4, n5]

    result = number_summary(numbers)

    print("Min:", result["min"])
    print("Max:", result["max"])
    print("Average:", result["average"])

except:
    print("Invalid input")


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 4: APPLY DISCOUNT
This code calculate the discount
with the input of price and the input of the discount

"""

def apply_discount(prices, discount):
    rate = discount / 100

    if len(prices) == 1:
        return [prices[0] - (prices[0] * rate)]
    elif len(prices) == 2:
        return [
            prices[0] - (prices[0] * rate),
            prices[1] - (prices[1] * rate)
        ]
    elif len(prices) == 3:
        return [
            prices[0] - (prices[0] * rate),
            prices[1] - (prices[1] * rate),
            prices[2] - (prices[2] * rate)
        ]
    else:
        return [
            prices[0] - (prices[0] * rate),
            prices[1] - (prices[1] * rate),
            prices[2] - (prices[2] * rate),
            prices[3] - (prices[3] * rate)
        ]


price_text = input("\nEnter prices separated by commas: ")
discount_value = int(input("Enter discount percentage: "))

try:
    price_text = price_text.split(",")

    p1 = float(price_text[0])
    p2 = float(price_text[1])

    if len(price_text) == 2:
        prices = [p1, p2]
    elif len(price_text) == 3:
        p3 = float(price_text[2])
        prices = [p1, p2, p3]
    else:
        p3 = float(price_text[2])
        p4 = float(price_text[3])
        prices = [p1, p2, p3, p4]

    discounted_prices = apply_discount(prices, discount_value)

    print("Original prices:", prices)
    print("Discounted prices:", discounted_prices)

except:
    print("Invalid input")


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 5: GREETING WITH OPTIONAL TITLE
This function prints a greeting to the name that you put on the input

"""

def create_greeting(name, title):
    name = name.strip()
    title = title.strip()

    if name == "":
        print("Invalid name")
    elif title == "":
        print("Hello", name)
    else:
        print("Hello", name, title)


user_name = input("\nEnter your name: ")
user_title = input("Enter your title (optional): ")

create_greeting(user_name, user_title)


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM 6: FACTORIAL
This function calculates the factorial of a number
It uses recursion

"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


factorial_input = input("\nEnter a number for factorial: ")

try:
    factorial_number = int(factorial_input)

    if factorial_number < 0:
        print("Invalid input")
    else:
        print("Factorial:", factorial(factorial_number))

except:
    print("Invalid input")


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
END 
in this archive i learn how use excatly the functions in python and 
that the functions need to be use almost all the times cause them help
us way to much to realize and operate inputs or sums, mults or things that 
are functions in a calculator 

"""

"""
REFERENCES

https://docs.python.org/3/tutorial/controlflow.html#defining-functions
https://www.programiz.com/python-programming/function
https://www.w3schools.com/python/python_functions.asp
https://realpython.com/defining-your-own-python-function/
https://recursospython.com/guias-y-manuales/funciones/

"""
