"""
1- Open the python interactive shell and do the following operations. The operands are 3 and 4.
    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
"""

print('\n--- Ejercicio 1 ---\n')
# Suma
print(f'Suma: {3 + 4}')

# Resta
print(f'Resta: {3 - 4}')

# Multiplicacion
print(f'Multiplicacion: {3 * 4}')

# Resto
print(f'Resto: {3 % 4}')

# Division
print(f'Division: {3 / 4}')

# Division entera
print(f'Division Entera: {3 // 4}')

# Exponente
print(f'Exponente: {3 ** 4}')

"""
2-  Write strings on the python interactive shell. The strings are the following:
    Your name
    Your family name
    Your country
    I am enjoying 30 days of python

"""
print('\n--- Ejercicio 2 ---\n')
print('Mi nombre: Luciano')
print('Mi apellido: Valenzuela')
print('Mi pais: Argentina')
print('Estoy disfrutando de 30 dias de Python!')

"""
3- Check the data types of the following data:
    10
    9.8
    3.14
    4 - 4j
    ['Asabeneh', 'Python', 'Finland']
    Your name
    Your family name
    Your country
"""
print('\n--- Ejercicio 3 ---\n')
print(f'10 es del tipo: {type(10)}')
print(f'9.8 es del tipo: {type(9.8)}')
print(f'3.14 es del tipo: {type(3.14)}')
print(f'4 - 4j es del tipo: {type(4 - 4j)}')
print(f'[Asabeneh, Python, Finland] es del tipo: ' + str(type(['Asabeneh', 'Python', 'Finland'])))
print(f'Luciano es del tipo: ' + str(type('Luciano')))
print(f'Valenzuela es del tipo: ' + str(type('Valenzuela')))
print(f'Argentina es del tipo: ' + str(type('Argentina')))

"""
4-  Write an example for different Python data types such as Number(Integer, Float, Complex),
    String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)
"""

print('\n--- Ejercicio 4 ---\n')
print('**** Numeros ****\n')
print(f'Enteros (2 + 2): {2 + 2}')
print(f'Flotante (3.5 * 2.1): {3.5 * 2.1}')
print(f'Numero complejo: {(2 + 3j) / (3 - 1j)}')
print('\n**** Cadenas ****\n')
print('Me gusta mucho la musica')
print('Me encantan los videojuegos RPG')
print('Me gustan las peliculas de terror')
print('\n**** Booleanos ****\n')
print('Me gusta la musica? --- True (Verdadero)')
print('No me gustan las peliculas de terror? --- False (Falso)')
print('\n**** Listas ****\n')
print(['Three Days Grace', 'Guns and Roses', 'Duki', 'Luis Miguel'])
print(['Arroz', 'Leche', 'Fideo', 'Yerba'])
print('\n**** Tuplas ****\n')
print((1, 2, 3, 4))
print(('Pan', 4, 'Miguel', 3.5))
print('\n**** Set ****\n')
print({3, 1, 5, 8})
print({'Tortugas Ninja', 'Spiderman', 'Superman', 'Batman', 2})
print('\n**** Diccionarios ****\n')
print([{
    'Nombre': 'Luciano',
    'Apellido': 'Valenzuela',
    'Pais': 'Argentina',
    'Comida Favorita': 'Milanesa Napolitana'
}])
# Importamos el dist del modulo math, que nos ayuda a calcular la distancia Eucliana entre dos puntos
from math import dist

print('\n**** Distancia Eucliana (10, 8) ****\n')
print(f'Distancia entre (2, 3) y (10, 8): {dist((2, 3), (10, 8))}')
