"""Calculate whether a fine must be paid according to:
the speed of the vehicle and the blood alcohol content.
"""

dist_1 = float(input('Distancia 1 [m]: '))
dist_2 = float(input('Distancia 2 [m]: '))
t = float(input('Tiempo [s]: '))

x = dist_1 - dist_2
# Convert velocity to km/h:
v = x/t * 3.6

if v < 1:
    print('Velocidad inválida.')
else:
    if v >= 1 and v <= 20:
        velocity_fine = 'Llamado de atención por baja velocidad.'
    elif v >= 21 and v <= 60:
        velocity_fine = 'Normal' 
    elif v >= 61 and v <= 80:
        velocity_fine = 'Llamado de atención por alta velocidad.'
    elif v >= 81 and v <= 120:
        velocity_fine = 'Multa tipo I'
    else:
        velocity_fine = 'Multa tipo II e inmovilización del vehículo.'
    print(velocity_fine)

# Alcohol screening test:
alcohol = float(input('Alcohol [mg de etanol/100 mL de sangre  total]: '))

if alcohol < 20:
    print('Alcohol inválido.')
else:
    if alcohol >= 20 and alcohol <= 39:
        alcohol_fine = 'Suspensión de la licencia de conducción entre seis (6) y doce (12) meses.'
    elif alcohol >= 40 and alcohol <= 99:
        alcohol_fine = 'Suspensión de la Licencia de Conducción entre uno (1) y tres (3) años.'
    elif alcohol >= 100 and alcohol <= 149:
        alcohol_fine = """- Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años.
        - Obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción
        en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.
        """
    else:
        alcohol_fine = """- Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción.
        - Obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción
        en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas.
        """
    print(alcohol_fine)
 