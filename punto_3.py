"""Show second by second the distance traveled by a sphere dropped from a building.
"""

height = float(input('Altura del edificio [m]: '))
g = 9.8
d = 0
t = 0
while d < height:
    print('Tiempo: %.2f s. Distancia: %.2f m.' % (t, d))
    t += 1
    d = (1/2) * g * t**2 # The initial velocity is assumed to be v = 0.
    
# Arrival of the object on the ground:
t_final = (2*height/g)**(1/2)
print('Tiempo: %.2f s. Distancia: %.2f m.' % (t_final, height))
