"""
# COVER PAGE

# 2530090_MartinezReyesJoseAlejandro
# Group: 103 / 1-1

"""

"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
PROBLEM: FIBONACCI SERIES
This code generates the real Fibonacci series the user decide how many digits want and they will be generated

"""

num_1 = 0
num_2 = 1
count = 0

print("Fibonazetai serie")

try:
    num_total_loop = int(input("set times \n"))

    if num_total_loop < 0:
        print("guatafa vro")

    else:
        while count < num_total_loop:
            print(num_1)

            new_number = num_1 + num_2
            num_1 = num_2
            num_2 = new_number

            count = count + 1

except ValueError:
    print("ERROR value incorrect")


"""
________________________________________________________________________________
________________________________________________________________________________

"""

"""
END
in this code i learn the sequences of fibunacci and how to apply that to get the digits 

"""

"""
REFERENCES

https://docs.python.org/3/tutorial/controlflow.html
https://www.programiz.com/python-programming/while-loop
https://www.w3schools.com/python/python_while_loops.asp
"""
