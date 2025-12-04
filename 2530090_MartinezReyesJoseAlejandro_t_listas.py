# ================================================================
# COVER PAGE
# ================================================================
# 2530090_MartinezReyesJoseAlejandro
# Group: 103 / 1-1
# Subject: Programming
# Topic: Tuples, Lists and Dictionaries
# ================================================================

# This file demonstrates the correct use of Python data structures:
# lists, tuples, and dictionaries.


# ================================================================
# BASIC CONCEPTS
# ================================================================
"""
Mutable: Can be modified after creation.
Immutable: Cannot be modified after creation.

List: Ordered, mutable collection.
Example: my_list = [item1, item2]

Tuple: Ordered, immutable collection.
Example: my_tuple = (10, 20)

Dictionary: Unordered, mutable collection using key-value pairs.
Example:
my_dict = {
    key1: value1,
    key2: value2
}
"""


# ================================================================
# PROBLEM 1: SHOPPING LIST BASICS (LIST)
# ================================================================
"""
Program:
- Lets the user enter product names
- Prints the complete list
- Shows how many items were added
- Allows searching for a product
"""

product_count = 0
product_list = []

while True:
    try:
        product_name = input("Enter a product (type 'end' to finish): ")

        if product_name.lower() == "end":
            break

        product_list.append(product_name)
        product_count += 1

    except ValueError:
        print("Invalid input.")
        continue

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        break

print("\nYour product list:")
for item in product_list:
    print(item)

print(f"You entered {product_count} products.")

search_name = input("Search for a product? (type 'no' to skip): ")

if search_name.lower() == "no":
    print("Program finished.")
else:
    if search_name in product_list:
        print(f"{search_name} is already on your list.")
    else:
        print(f"{search_name} is not in your list.")


# ================================================================
# PROBLEM 2: POINTS AND DISTANCE WITH TUPLES
# ================================================================
"""
Program:
- Asks for 2 coordinates
- Returns:
    - Euclidean distance
    - Midpoint
"""

print("Coordinate System")

while True:
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

    except ValueError:
        print("Invalid value.")
        continue

    point1 = (x1, y1)
    point2 = (x2, y2)

    import math

    def euclidean_distance(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    distance = euclidean_distance(point1, point2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point 1:", point1)
    print("Point 2:", point2)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

    break


# ================================================================
# PROBLEM 3: PRODUCT CATALOG WITH DICTIONARY
# ================================================================
"""
Program:
- Contains a dictionary of products and prices
- Allows purchasing items
- Calculates total cost
"""

catalog = {
    "apple": 6,
    "soda": 12,
    "chips": 5,
}

purchased_items = []
total_cost = 0

print("Available Products:")
print(catalog)

while True:
    try:
        chosen_item = input("Choose a product (type 'end' to finish): ").strip().lower()

        if chosen_item == "end":
            print("Purchase summary:")
            for item in purchased_items:
                print(item)
            print(f"Total amount: {total_cost} $.")
            break

        quantity = int(input("Quantity: "))

    except ValueError:
        print("Invalid input.")
        continue

    if not chosen_item:
        print("Empty input not allowed.")
        continue

    if chosen_item in catalog:
        item_price = catalog[chosen_item]
        subtotal = item_price * quantity
    else:
        print("Product not found.")
        continue

    total_cost += subtotal
    purchased_items.append(chosen_item)


# ================================================================
# PROBLEM 4: STUDENT GRADES (DICT + LIST)
# ================================================================
"""
Program:
- Searches for a student by name
- Shows grades
- Shows average
- States whether they passed
"""

student_records = {
    "Gael": [8, 7, 9],
    "Arael": [6, 7, 7],
    "Renata": [9, 10, 8],
    "Martha": [8, 6, 10],
}

student_search = input("Search for a student: ").capitalize()

if student_search in student_records:
    grades = student_records[student_search]
    average = sum(grades) / len(grades)

    print("Grades:", grades)
    print("Average:", average)
    print("Passed:", average >= 7)
else:
    print("Student not found.")


# ================================================================
# PROBLEM 5: WORD FREQUENCY (LIST + DICT)
# ================================================================
"""
Program:
- Splits a sentence into words
- Counts occurrences of each one
"""

word_count = {}

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Words:")
print(words)

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
print(word_count)


# ================================================================
# PROBLEM 6: CONTACT BOOK (DICTIONARY CRUD)
# ================================================================
"""
Program allows:
- Adding contacts
- Searching contacts
- Deleting contacts
- Exiting
"""

contact_book = {
    "Renata": 1234,
    "Gael": 5432,
    "Martha": 1324,
    "Arael": 2431,
}

while True:
    print("Choose an action:")
    action = input("Add, Search, Delete, Exit: ").lower()

    if action == "add":
        name = input("New contact name: ").title()
        phone = input("Phone number: ")
        contact_book[name] = phone
        print("Contact added.")

    elif action == "search":
        name = input("Contact name: ").title()
        if name in contact_book:
            print("Phone:", contact_book[name])
        else:
            print("Contact not found.")

    elif action == "delete":
        name = input("Contact to delete: ").title()
        removed = contact_book.pop(name, None)
        if removed is None:
            print("Contact not found.")
        else:
            print(f"Removed: {name} -> {removed}")

    elif action == "exit":
        print("Goodbye :)")
        break

    else:
        print("Invalid option.")


# ================================================================
# FINAL CONCLUSION
# ================================================================
"""
Lists = Ordered & editable
Tuples = Ordered & not editable
Dictionaries = Key-value storage

These structures help organize and process data efficiently.
"""


# ================================================================
# REFERENCES
# ================================================================
"""
w3schools.com/python/python_lists.asp
w3schools.com/python/python_tuples.asp
w3schools.com/python/python_dictionaries.asp
docs.python.org/3/tutorial/datastructures.html
"""