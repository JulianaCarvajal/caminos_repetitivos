"""Show the number of people in a family for each generation
(up to a given generation).
"""

generation = int(input('Generación: '))

if generation < 0:
    print('Generación inválida.')
else:
    print('En la generación 0 hay 1 persona.')
    for i in range(1, generation):
        people = 2**(i)
        print(f'En la generación {i} hay {people} personas.')
    print(f'El número total de personas, hasta la generación {i+1}, es: {2**(i+1)}.')


