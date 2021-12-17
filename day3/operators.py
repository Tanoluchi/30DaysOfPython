print('\n--- Ejercicios Dia 3 ---\n')
# Variables declaration (Exercises 1 - 3)
age = 20
height = 1.60
complex_number = (1 + 1j) * (2 - 3j)

# Exercise 4
# We ask the user to enter the data
base = float(input('Insert the base of the triangle: '))
height = float(input('Insert the height of the triangle: '))

# The area is calculated
area_triangle = 0.5 * base * height

print(f'\nThe area of the triangle is: {area_triangle}\n')
print('\n------------------------------------------------\n')

# Exercise 5
side_a = float(input('Insert the side a of the triangle: '))
side_b = float(input('Insert the side b of the triangle: '))
side_c = float(input('Insert the side c of the triangle: '))

# The perimeter is calculated
perimeter_triangle = side_a + side_b + side_c

print(f'\nThe perimeter of the triangle is: {perimeter_triangle}')
print('\n------------------------------------------------\n')

# Exercise 6
length = float(input('Insert length of the rectangle: '))
width = float(input('Insert width of the rectangle: '))

# The area is calculated
area_rectangle = length * width

# The perimeter is calculated
perimeter_rectangle = 2 * (length + width)

print(f'\nThe area of the rentangle is {area_rectangle} and perimeter is {perimeter_rectangle}')
print('\n------------------------------------------------\n')

# Exercise 7
radio_circle = float(input('Insert radio of the circle: '))
pi = 3.14

# The area is calculated
area_circle = pi * (radio_circle ** 2)

# The Circumference is calculated
circumference = 2 * pi * radio_circle

print(f'The area of the circle is {radio_circle} and circumference is {circumference}')
print('\n------------------------------------------------\n')

# Exercise 8
x_intercept = 3
y_intercept = 4
slope_intercept = ((2*3)-2)
print(f'y = 2x - 2 ==> y = {(2 * 3) - 2}')
print(f'y = 2x - 2 ==> y = {(4 + 2) / 2}')
print('\n------------------------------------------------\n')

# Exercise 9
y1 = 2
x1 = 2
y2 = 10
x2 = 6
slope_result =  (y2 - y1) / (x2 - x1)
distance_euclidean = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
print(f'The slope is {slope_result} and the distance euclidean is {distance_euclidean}')
print('\n------------------------------------------------\n')

# Exercise 10
print(f'Compare slope the task 8 and task 9: {slope_result == slope_intercept}')

# Exercise 11
x = pow(1.5, 0.5)
y = ((-x ** 2) + (6 * -x) + 9)
print(round(y))
print('\n------------------------------------------------\n')

# Exercise 12
python_length = len("Python")
dragon_length = len("Dragon")
print(f'The length of "Python" is {python_length}')
print(f'The length of "Dragon" is {dragon_length}')

print(python_length != dragon_length)
print('\n------------------------------------------------\n')

# Exercise 13
print('on' in 'python' and 'on' in 'dragon')
print('\n------------------------------------------------\n')

# Exercise 14
print('jargon' in 'I hope this course is not full of jargon')
print('\n------------------------------------------------\n')

# Exercise 15
print(not('on' in 'python' and 'on' in 'dragon'))
print('\n------------------------------------------------\n')

# Exercise 16
python_length = float(python_length)
print(type(python_length))
python_length = str(python_length)
print(type(python_length))
print('\n------------------------------------------------\n')

# Exercise 17
number = int(input('Insert a number integer: '))
even = (number % 2) == 0
print(f'The number {number} is even? : {even}')
print('\n------------------------------------------------\n')

# Exercise 18
number_converted = int(2.7)
print(number_converted)
division = 7 // 3
print(f'The value the floor division of 7 by 3 is equal to the int converted value of 2.7? : {division == number_converted}')
print('\n------------------------------------------------\n')

# Exercise 19
string1 = '10'
number2 = 10

print(f'The type of "10" is equal to type of 10? : {type(string1) == (number2)}')
print('\n------------------------------------------------\n')

# Exercise 20
print(int(9.8) == 10)
print('\n------------------------------------------------\n')

# Exercise 21
hours = int(input('Insert the hours: '))
rate_per_hour = int(input('Insert the rate per hour: '))

print(f'Your weekly earning is: {hours * rate_per_hour}')
print('\n------------------------------------------------\n')

# Exercise 22
years_life = int(input('Insert number of years you have lived: '))
seconds = (years_life * (365*24*60*60))

print(f'You have lived for : {seconds}')
print('\n------------------------------------------------\n')

# Exercise 23
for i in range(1, 6):
    if i == 1: print("1 1 1 1 1")
    else: print(f'{i} 1 {i} {i ** 2} {i ** 3}')
        
