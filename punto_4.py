"""La siguiente gráfica muestra el comportamiento de los descendientes y ascendientes de una persona,
si asumimos que esta persona es la generación 0, la generación 1 serán dos personas (sus padres)
la generación 2 serán 4 personas (sus abuelos) y así sucesivamente.

Debe crear un programa que dada una generación (mayor o igual a cero):
- Le indique al usuario el número total de personas de la familia
(de todas las generaciones hasta la generación dada).
- Muestre el número de personas de cada generación mientras hace el cálculo.
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
