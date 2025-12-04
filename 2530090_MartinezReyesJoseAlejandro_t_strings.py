# ================================================================
# COVER PAGE
# ================================================================
# 2530090_MartinezReyesJoseAlejandro
# Group: 103 / 1-1
# ================================================================

# In this file, I use different programs to show the correct use
# of strings using functions and methods.


# ================================================================
# WHAT IS A STRING?
# ================================================================
"""
In Python, a string is any group of characters written between
double quotes "" or single quotes ''.
Strings can contain letters, numbers, and symbols.

Basic operations that can be performed with strings:
- Concatenation using +
- f-strings to join text with numbers
- Methods to normalize text such as:
  upper()   -> converts to uppercase
  lower()   -> converts to lowercase
  title()   -> capitalizes each word
  strip()   -> removes spaces at the beginning and end
  len()     -> counts the number of characters
"""


# ================================================================
# FIRST PROGRAM: FULL NAME FORMATTER (NAME + INITIALS)
# ================================================================
"""
This program asks for the user's full name, removes extra spaces,
applies title format, and shows the full name and initials.
"""

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value.title()
        else:
            print("Empty input is not allowed. Try again.\n")

def full_name(first_name, middle_name, last_name1, last_name2):
    return f"{first_name} {middle_name} {last_name1} {last_name2}"

first_name = get_non_empty("Put your first name: ")
middle_name = get_non_empty("Put your middle name: ")
last_name1 = get_non_empty("Put your first last name: ")
last_name2 = get_non_empty("Put your second last name: ")

initials = f"{first_name[0]}. {middle_name[0]}. {last_name1[0]}. {last_name2[0]}."
name = full_name(first_name, middle_name, last_name1, last_name2)

print("Your full name is:", name)
print("Your initials:", initials)


# ================================================================
# SECOND PROGRAM: EMAIL CHECKER
# ================================================================
"""
This program checks if the email contains:
- Only one "@"
- A dot "." in the domain
- No spaces
"""

def check_email():
    email = input("Enter your email: ").strip()

    if email == "":
        print("Email cannot be empty.")
        return

    if " " in email:
        print("Spaces are not allowed.")
        return

    at_count = email.count("@")
    if at_count != 1:
        print("Email must contain exactly one '@'.")
        return

    domain_position = email.find("@")
    domain = email[domain_position + 1:]

    if "." not in domain:
        print("The domain must contain a dot.")
        return

    print("Full email:", email)
    print("Domain:", domain)
    print("Number of '@' symbols:", at_count)

check_email()


# ================================================================
# THIRD PROGRAM: PALINDROME CHECKER
# ================================================================
"""
This program checks if a phrase is a palindrome.
A palindrome reads the same forwards and backwards.
"""

def check_palindrome(phrase):
    if phrase.strip() == "":
        print("Error: The phrase cannot be empty.")
        return

    normalized = phrase.lower().replace(" ", "")

    if len(normalized) < 3:
        print("Error: The phrase must have at least 3 characters.")
        return

    is_palindrome = normalized == normalized[::-1]

    print("Normalized phrase:", normalized)
    print("Is palindrome:", is_palindrome)

text = input("Enter a phrase: ")
check_palindrome(text)


# ================================================================
# FOURTH PROGRAM: SENTENCE WORD STATISTICS
# ================================================================
"""
This program shows:
- Total number of words
- First word
- Last word
- Shortest word
- Longest word
"""

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: Sentence cannot be empty.")
else:
    words = sentence.split()

    if len(words) == 0:
        print("Error: The sentence must contain at least one word.")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)

        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)


# ================================================================
# FIFTH PROGRAM: PASSWORD STRENGTH CHECKER
# ================================================================
"""
This program checks if a password is weak, medium, or strong
based on length and content.
"""

password_input = input("Enter your password: ").strip()

if password_input == "":
    print("Password cannot be empty.")
else:
    length = len(password_input)

    has_upper = False
    has_lower = False
    has_digit = False
    has_alnum = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char.isalnum():
            has_alnum = True

    if length < 6:
        strength = "weak"
    elif length >= 6 and has_digit and (has_upper or has_lower):
        strength = "medium"
    elif length >= 8 and has_upper and has_lower and has_digit and has_alnum:
        strength = "strong"
    else:
        strength = "weak"

    print("Password strength:", strength)


# ================================================================
# SIXTH PROGRAM: PRODUCT LABEL (30 CHARACTERS)
# ================================================================
"""
This program creates a label with exactly 30 characters.
If it is shorter, it adds spaces.
If it is longer, it cuts the text.
"""

product = input("Enter product name: ").strip()
cost = input("Enter product price: ").strip()

if product == "":
    print("Error: Product name cannot be empty.")
else:
    try:
        amount = float(cost)

        if amount <= 0:
            print("Error: Price must be positive.")
        else:
            text = str(amount)
            label = f"{product} - ${text}"

            if len(label) < 30:
                label = label + " " * (30 - len(label))
            else:
                label = label[:30]

            print(f'Label: "{label}"')

    except ValueError:
        print("Error: Price must be a valid number.")


# ================================================================
# FINAL COMMENT
# ================================================================
"""
In all these programs, string methods such as strip(), lower(),
upper(), title(), and len() are very important.
They help clean user input and prevent errors in programs.
This is why strings are essential in Python programming.
"""


# ================================================================
# REFERENCES
# ================================================================
"""
https://youtu.be/CCUNuqqn7PQ
https://youtu.be/9k91jETchkI
https://youtu.be/Pr-9wkSJDJk
https://youtu.be/OvafT2HL0uU
https://youtu.be/WSQvaPHsm64
https://youtu.be/tb6EYiHtcXU
"""
