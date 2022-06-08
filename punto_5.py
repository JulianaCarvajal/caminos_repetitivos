"""Se debe crear un programa que dada una longitud en cuadros (mayor a cero),
genere un tablero, como en la siguiente imagen (Es un tablero con una longitud de 8x8):
"""

full_line = "***"
empty_line = "   "

size = int(input('Ingrese la longitud del tablero: '))

board = ''
if size == 1:
    board = 3*(empty_line + "\n")
elif size%2 == 0:
    line_1 = 3*(int(size/2)*(empty_line + full_line) + "\n")
    line_2 = 3*(int(size/2)*(full_line + empty_line) + "\n")
    for i in range(int(size/2)):
        board += line_1 + line_2
else:
    line_1 = 3*(empty_line + int((size-1)/2)*(full_line + empty_line) + "\n")
    line_2 = 3*(full_line + int((size-1)/2)*(empty_line + full_line) + "\n")
    for i in range(int((size-1)/2)):
        board += line_1 + line_2
    board += line_1
print(board)
