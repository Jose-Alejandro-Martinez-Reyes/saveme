"""
COVER PAGE

2530090_MartinezReyesJoseAlejandro
Group: 103 / 1-1

"""

"""
________________________________________________________________________________
________________________________________________________________________________

"""

data_list = []

def create_item(item):
    data_list.append(item)
    print("Item created successfully")


def read_items():
    if len(data_list) == 0:
        print("No items to display")
    else:
        print("Current items:")
        for i, item in enumerate(data_list):
            print(i, ":", item)


def update_item(index, new_item):
    if index < 0 or index >= len(data_list):
        print("Invalid index")
    else:
        data_list[index] = new_item
        print("Item updated successfully")


def delete_item(index):
    if index < 0 or index >= len(data_list):
        print("Invalid index")
    else:
        data_list.pop(index)
        print("Item deleted successfully")


while True:
    print("\n--- CRUD MENU ---")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    option = input("Select an option: ")

    if option == "1":
        item = input("Enter new item: ")
        create_item(item)

    elif option == "2":
        read_items()

    elif option == "3":
        read_items()
        try:
            index = int(input("Enter index to update: "))
            new_item = input("Enter new value: ")
            update_item(index, new_item)
        except ValueError:
            print("Invalid input")

    elif option == "4":
        read_items()
        try:
            index = int(input("Enter index to delete: "))
            delete_item(index)
        except ValueError:
            print("Invalid input")

    elif option == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option")


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
END
In this program I learned how to use functions, lists, loops and conditionals in sequence for the correct 
In this program I learned how to correctly use input statements,
delete operations, and lists in order to make a CRUD system work properly.

"""

"""
REFERENCES

https://docs.python.org/3/tutorial/datastructures.html
https://www.programiz.com/python-programming/list
https://www.w3schools.com/python/python_lists.asp
"""
