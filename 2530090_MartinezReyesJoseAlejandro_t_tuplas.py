"""
Tuplas, listas y diccionarios.
Antes de definir estos elementos de python tenemos que comprender el significado de  lo que es mutable e inmutable, cuando 
hablamos de elementos mutables se refiere a los que pueden ser modificados, por el contrario cuando nos referimos a elementos
inmutables son aquellos que no pueden ser modificados.

Listas: Se trata de una colección de elementos ordenados, estas pueden contener elementos de todo tipo ya sea palabras, numeros, 
e inclusive otras listas, a su vez estas son mutaables, ejemplo de la estructura:
lista = [elemento_1, elemento_2, elemento_3, etc]

Tuplas: Estas son semejantes a las listas, siendo conjuntos ordenados de datos, e inmutables, ejemplo de su estructura:
tupla = (640, 480)

Diccionarios: Estas son listas no ordenadas y mutables, en las que se relacionan los valores a palabras clave, ejemplo de su
estructura:
diccionario = {
clave_1: valor_1
clave_2: valor_2
clave_3: valor_3
etc.
}
"""


"""
PROBLEM 1: Shopping list basics.

El programa va a constar en una lista en la que puedes ingresar nuevos productos.
input.- nuevos productos.
output.- lista de productos, cantidad total de productos, y en caso de buscar algun producto
true/false dependiendo de si se encuentra o no.

"""
product_counter = 0
products_lista = []

while True:
    try:
        product = input("Set your product (if you wanna end the list write 'end'): ")

        if product.lower() == 'end':
            break

        products_lista.append(product)
        product_counter += 1

    except ValueError:
        print("Carácter inválido.")
        continue

    except KeyboardInterrupt:
        print("\nEl programa fue interrumpido.")
        break

print("\nYour product list:")
for item in products_lista:
    print(item)

print(f"You get {product_counter} products.")

search = input("Do you wanna search a product in your list (if you don't write 'no')? ")

if search.lower() == "no":
    print("Program finished.")
else:
    if search in products_lista:
        print(f"You already have {search}.")
    else:
        print(f"{search} is not in your list.")

"""
CASOS DE PRUEBA:
Normal.-
inpunt: dato_1, dato_2, dato_3
output: You get 3 products.
busqueda (opcional): dato_2 / You already have dato_2.

Borde.-
input: dato_1, dato_2, dato_3, (input en blanco), dato_4
output: You get 5 products.
busqueda (opcional): (input en blanco)/ You already have .

Error.- 
input: "end"(finalizar el programa).
output: (vacio)
busqueda: (input vacio)/  is not in your list.
"""


"""
PROBLEM 2: Points and distances with tuples.

Crearas dos tuplas punto_a y punto_b con entradas numericas y genera una tercer coordenada que seria el punto medio, además calcula
la distncia euclidiana.
input: (x1,x2), (y1,y2)

output:
"Point A:" (x1, y1)
"Point B:" (x2, y2)
"Distance:" <distance>
"Midpoint:" (mx, my)

Validaciones: solo necesitamos que las entradas se puedan transformar en float.
"""

print("Sistema de coordenadas. ")
while True:
    try:
        x1 = int(input("Ingresa tu coordenada x1: "))
        y1 = int(input("Ingresa tu coordenada y1: "))

        x2 = int(input("Ingresa tu coordenada x2: "))
        y2 = int(input("Ingresa tu coordenada y2: "))
     
    except ValueError:
        print("Carácter inválido.")
        continue

    tupla_x=(x1,y1)
    tupla_y=(x2,y2)

    import math
    def d_euclidiana(p1, p2):
        return math.sqrt((p2[0] - p1[0])*2 + (p2[1] - p1[1])*2)

    cord_1 = (x1, y1)
    cord_2 = (x2, y2)
    dist = d_euclidiana(cord_1, cord_2)

    pm=((x1-x2)/2, (y1-y2)/2)

    print("Coordenadas: ")
    print(tupla_x)
    print(tupla_y)

    print("Distancia euclidiana: ")
    print(dist)

    print("Punto medio: ")
    print(pm)

    break


"""
CASOS DE PRUEBA:
Normal.-
input: (5,5),(8,8)
utput:
(5,5)
(8,8)
4.2426
(-1.5, -1.5)

Borde.-
input:(-10, -10),(-20, 20)
output:
(-10, -10)
(-20, 20)
31.6227
(5, -15)

Error.-
input:e
output: Carácter invalido (reinicia).
"""


"""
PROBLEM 3: Product catalog with dictionary.

A partir de un diccionario con minimo 3 productos, busca entre los diccionarios los productos y el precio de los mismos, además
de responder con la cantidad a pagar en la compra de una cantidad ingresada previamente de producto.

Input.- producto, cantidad
Output.- producto existente y/n, costo individual, costo total.
Validación.- no puede haber inputs en blanco o con carcteres incorrectos.
"""

Products_dictionary={
    "apple": 6,
    "soda": 12,
    "chips": 5,
}

shopping_list= []
price_counter = 0
print("Products. \nMenu: ")
print(Products_dictionary)

while True:
    try:
        product_buy = input("What product do you want (write 'end to finish the program'): ").strip().lower()

        if product_buy == "end":
            print("Finishing program.")
            for shopping_list in shopping_list:
                print(shopping_list)
            print(f"Your total is {price_counter} $.")
            break

        quantity = int(input("Quantity: "))

    except ValueError:
        print("invalid character.")
        continue
        
    except KeyboardInterrupt:
        print("\nEl programa fue interrumpido.")
        break

    if not product_buy:
        print("No empty input please.")
        continue

    if product_buy in Products_dictionary:
        unit_price = Products_dictionary[product_buy]
        total = unit_price * quantity
    else:
        print("Product not found.")
        continue
        
    price_counter += total
    shopping_list.append(product_buy)

"""
CASOS DE PRUEBA:
Normal:
input.- apple/ 2
output.- apple / Your total is 12 $.

Borde:
input.- apple/ 1, apple/1, apple/ 1, (inputs repetidos).
output.- apple/ apple/ apple / Your total is 18 $.

Error:
input.- apple / -1 
output.- apple / Your total is -6 $ (output incorrecto).
"""


"""
PROBLEM 4: Student grades with dict and list.
Crea un diccionario inicial que contenga al menos 3 estudiantes y sus calificaciones en forma de listas dentro del mismo 
diccionario, a partir de dicho diccionario se realizrá.
input.- nombre de un alumno.
output.-
student_existence = true
lista de calificaciones
promedio
aprobado y/n
student_existence = false
message: error.
"""
   
students = {
    "Gael": [8, 7, 9],
    "Arael": [6, 7, 7],
    "Renata": [9, 10, 8],
    "Martha": [8, 6, 10],
}

student_search = input("Search your student: ")

student_search = student_search.capitalize()

if student_search in students:
    print("Grades:")
    print(students[student_search])

    grades = students[student_search]
    average = sum(grades) / len(grades)

    print("Average:", average)

    if average < 7:
        print("Passed: false.")
    else:
        print("Passed: true.")
else:
    print("Student not found.")

"""
CASOS DE PRUEBA:
Normal:
input.- Gael

Output.-
Grades:
[8, 7, 9]
Average: 8.0
Passed: true

Borde:
input.- arael

Output.-
Grades:
[6, 7, 7]
Average: 6.666666666666667
Passed: false.

Error:
input.- angel

Output.-
Student not found.
"""


"""
PROBLEM 5: Word frequency counter (list + dict).
Tras ingresar una oracion cuenta la cantidad de veces que cada palabra es usada.
input.- oración (sentence).

output.-
lista de palabras.
lista de frecuencias
palabra mas usada, si son dos cualquiera vale.
"""

output_dic = {}

sentence = input("Write your sentence: ")
words = sentence.split()

print("Words in your sentence: ")
print(words)

for w in words:
    if w in output_dic:
        output_dic[w] += 1
    else:
        output_dic[w] = 1
print("Words frequency: ")
print(output_dic)

"""
CASOS DE PRUEBA:
Normal.-
input: 'la frase de prueba repite la palabra frase'

output:
['la', 'frase', 'de', 'prueba', 'repite', 'la', 'palabra', 'frase']
Words frequency:
{'la': 2, 'frase': 2, 'de': 1, 'prueba': 1, 'repite': 1, 'palabra': 1}

Borde.-
input: ' La frase, contiene signos de puntuación y mayúsculas.'

output:
Words in your sentence:
['La', 'frase,', 'contiene', 'signos', 'de', 'puntuación', 'y', 'mayúsculas.']
Words frequency:
{'La': 1, 'frase,': 1, 'contiene': 1, 'signos': 1, 'de': 1, 'puntuación': 1, 'y': 1, 'mayúsculas.': 1}

Error.-
input: ' Lafrasenocontieneespaciosycontienesignosalgebraicos+-*'

output:
Words in your sentence:
['Lafrasenocontieneespaciosycontienesignosalgebraicos+-*']
Words frequency:
{'Lafrasenocontieneespaciosycontienesignosalgebraicos+-*': 1}
"""


"""
PROBLEM 6:  Simple contact book (dictionary CRUD).

Genera un contact book con un diccionario al que se le puede buscar un contacto, añadir un contacto o borrar un contacto.
input.-
action.
name (depende la accion).
phone (solo en añadir).

output.-
Para añadir:
"Contact saved:" name, phone
Para "buscar":
Si existe: "Phone:" phone
Si no existe: "Error: contact not found"
Para "borrar":
Si existe: "Contact deleted:" name
Si no existe: "Error: contact not found"
"""

contacts = {
    "Renata":1234,
    "Gael":5432,
    "Martha":1324,
    "Arael":2431,
    }

while True:
    print("What action do you wanna do? ")
    wanna = input("Add, Search, Delete, Exit: ")
    wanna = wanna.lower()

    if wanna == "add":
        new_name = input("New contact name: ").title()
        new_phone = input("New phone number: ")
        contacts[new_name] = new_phone
        print("New contact added sucesfully. ")
        continue

    if wanna == "search":
        searched = input("Name to search: ").title()
        if searched in contacts:
            print(searched)
            print("phone number:")
            print(contacts[searched])
        else:
            print("Error: contact not found.")
        continue

    if wanna == "delete":
        contact_del = input("Contact for delete (name): ").title()
        removed = contacts.pop(contact_del, None)
        if removed is None:
            print("Error: contact not found.")
        else:
            print(f"Deleted: {contact_del} -> {removed}")
            
        continue

    if wanna == "exit":
        print("Goodbye :)")
        break

"""
CASOS DE PRUEBA:
Normal: 
Input.- search / renata 
output.-
Renata
phone number:
1234

Borde:
Input.- diana / 1234
output.- 
New contact added sucesfully.

Error:
Input.- delete / ken
output.-
Error: contact not found.
"""

"""
CONCLUSIONES:

"""

"""
REFERENCIAS:
1)
2)
3)
4)
5)
"""