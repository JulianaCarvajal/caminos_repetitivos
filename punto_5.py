"""Se debe crear un programa que dada una longitud en cuadros (mayor a cero),
genere un tablero, como en la siguiente imagen (Es un tablero con una longitud de 8x8):
"""

linea_llena = "***"
linea_vacia = "   "

size = int(input('Ingrese la longitud del tablero: '))

tablero = ''
if size == 1:
    tablero = 3*(linea_vacia + "\n")
elif size%2 == 0:
    linea_1 = 3*(int(size/2)*(linea_vacia + linea_llena) + "\n")
    linea_2 = 3*(int(size/2)*(linea_llena + linea_vacia) + "\n")
    for i in range(int(size/2)):
        tablero += linea_1 + linea_2
else:
    linea_1 = 3*(linea_vacia + int((size-1)/2)*(linea_llena + linea_vacia) + "\n")
    linea_2 = 3*(linea_llena + int((size-1)/2)*(linea_vacia + linea_llena) + "\n")
    for i in range(int((size-1)/2)):
        tablero += linea_1 + linea_2
    tablero += linea_1
print(tablero)

