import math

"""
1- 
    - Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    - Write a python comment saying 'Day 2: 30 Days of python programming'
    - Declare a first name variable and assign a value to it
    - Declare a last name variable and assign a value to it
    - Declare a full name variable and assign a value to it
    - Declare a country variable and assign a value to it
    - Declare a city variable and assign a value to it
    - Declare an age variable and assign a value to it
    - Declare a year variable and assign a value to it
    - Declare a variable is_married and assign a value to it
    - Declare a variable is_true and assign a value to it
    - Declare a variable is_light_on and assign a value to it
    - Declare multiple variable on one line

"""
print('\n--- Ejercicio 1 ---\n')
# - Write a python comment saying 'Day 2: 30 Days of python programming'
print('Dia 2: 30 Dias de programacion en Python')
# - Declaration of variables
first_name = 'Luciano'
last_name = 'Valenzuela'
full_name = first_name + last_name
country = 'Argentina'
city = 'Corrientes'
age = 20
year = 2021
is_married = False
is_true = True
is_light_on = True
anime, film, book = 'ID:invaded', 'Taxi Driver', 'Lore'

"""
2-
    - Check the data type of all your variables using type() built-in function

    - Using the len() built-in function, find the length of your first name
    - Compare the length of your first name and your last name

    - Declare 5 as num_one and 4 as num_two
    - Add num_one and num_two and assign the value to a variable total
    - Subtract num_two from num_one and assign the value to a variable diff
    - Multiply num_two and num_one and assign the value to a variable product
    - Divide num_one by num_two and assign the value to a variable division
    - Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    - Calculate num_one to the power of num_two and assign the value to a variable exp
    - Find floor division of num_one by num_two and assign the value to a variable floor_division

    - The radius of a circle is 30 meters.
    - Calculate the area of a circle and assign the value to a variable name of area_of_circle
    - Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    - Take radius as user input and calculate the area.

    - Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

    - Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
print('\n--- Ejercicio 2 ---\n')
print(f'Tipo de variable de first_name: {type(first_name)}')
print(f'Tipo de variable de last_name: {type(last_name)}')
print(f'Tipo de variable de full_name: {type(full_name)}')
print(f'Tipo de variable de country: {type(country)}')
print(f'Tipo de variable de city: {type(city)}')
print(f'Tipo de variable de age: {type(age)}')
print(f'Tipo de variable de year: {type(year)}')
print(f'Tipo de variable de is_married: {type(is_married)}')
print(f'Tipo de variable de is_true: {type(is_true)}')
print(f'Tipo de variable de is_light_on: {type(is_light_on)}')
print(f'Tipo de variable de anime: {type(anime)}')
print(f'Tipo de variable de film: {type(film)}')
print(f'Tipo de variable de book: {type(book)}')
print('\n------------------------------------\n')
print(f'La longitud de mi nombre es de: {len(first_name)}')
print(f'La longitud de mi apellido es de: {len(last_name)}')
print('\n------------------------------------\n')
num_one = 5
num_two = 4

total = num_one + num_two
print(f'La suma de {num_one} y {num_two} es de: {total}')

diff = num_one - num_two
print(f'La resta de {num_one} y {num_two} es de: {diff}')

product = num_one * num_two
print(f'El producto de {num_one} y {num_two} es de: {product}')

division = num_one / num_two
print(f'La division entre {num_one} y {num_two} es de: {division}')

remainder = num_one % num_two
print(f'La resto de {num_one} y {num_two} es de: {remainder}')

exp = num_one ** num_two
print(f'El exponencial de {num_one} y {num_two} es de: {exp}')

floor_division = num_one // num_two
print(f'La division entera entre {num_one} y {num_two} es de: {floor_division}')

print('\n------------------------------------\n')
radius = 30

area_of_circle = math.pi * (radius ** 2)
print(f'El area de un circulo con un radio de {radius} metros es de: {area_of_circle}')

circum_of_circle = 2 * math.pi * radius
print(f'La circunferencia de un circulo con el radio de {radius} metros es de: {circum_of_circle}')

radius = float(input('Ingrese el radio del circulo: '))

area_of_circle = math.pi * (radius ** 2)
print(f'El area de un circulo con un radio de {radius} metros es de: {area_of_circle}')

print('\n------------------------------------\n')
help('keywords')
