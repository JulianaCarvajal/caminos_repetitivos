"""El funcionamiento de los radares de velocidad se basa en un principio
básico de la cinéticaque establece v=x/t, donde:

v: velocidad
x: posición - distancia
t: tiempo

El radar envía dos haces de luz en cierto tiempo (en segundos) y obtiene la distancia del
vehículo al radar en cada haz de luz enviado, así puede calcular la velocidad del vehículo
y establecer si está en los límites permitidos o por el contrario debe ser multado.
El  radar  toma estos datos en metros.

Dadas las dos distancias obtenidas del vehículo y el tiempo,
calcular si debe pagar una multa de acuerdo conla siguiente tabla:


| Velocidad (km/h) | Multa                                       |
------------------------------------------------------------------
| De 1 a 20        | Llamado de atención por baja velocidad      |
| De 21 a 60       | Normal                                      |
| De 61 a 80       | Llamado de atención por alta velocidad      |
| De 81 a 120      | Multa tipo I                                |
| Más de 120       | Multa tipo II e inmovilización del vehículo |

En caso de tener multa por velocidad, se le practica un examen de alcoholemia al conductor 
que acarrea multas adicionales de acuerdo con la siguiente norma:

•Entre 20 y 39 mg de etanol/l00 ml de sangre total, además de las sanciones previstas en la presente
ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses.

•Primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de sangre total, adicionalmente a la
sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años.

•Segundo grado de embriaguez entre 100 y 149 mg de etanol/100 ml de sangre total, adicionalmente a la
sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años,
y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y
drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.

•Tercer grado de embriaguez, desde 150 mg de etanol/100 ml de sangre total en adelante, adicionalmente a la
sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de
Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia
y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas.
"""

dist_1 = float(input('Distancia 1 [m]: '))
dist_2 = float(input('Distancia 2 [m]: '))
t = float(input('Tiempo [s]: '))

x = dist_2 - dist_1
# Convert velocity to km/h:
v = x/t * 3.6
velocity_fine = " "
alcohol_fine = " "

if v < 1:
    print('Velocidad inválida.')
else:
    if v >= 1 and v <= 20:
        velocity_fine = 'Llamado de atención por baja velocidad.'
    elif v >= 21 and v <= 60:
        velocity_fine = 'Normal' 
    elif v >= 61 and v <= 80:
        velocity_fine = 'Llamado de atención por alta velocidad.'
    else:
        if v >= 81 and v <= 120:
            velocity_fine = 'Multa tipo I'
        else:
            velocity_fine = 'Multa tipo II e inmovilización del vehículo.'
        print("Es necesario realizar un examen de alcoholemia al conductor.")
        
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
                alcohol_fine = ("- Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años.\n" 
                "- Obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción\n"
                "en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.")
           
            else:
                alcohol_fine = ("- Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción.\n"
                "- Obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción\n"
                "en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas.")
    print(velocity_fine)
    print(alcohol_fine)