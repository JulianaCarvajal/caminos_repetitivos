"""En 1590 Galileo presentó las leyes de la caída libre:
    Sin resistencia los cuerpos caen a la misma velocidad independientemente de su masa, forma y composición.
    Cuando se lanza un objeto la distancia que recorre es proporcional al tiempo d = v*t ± (1/2)*g*t^2, donde:
        
        • d es la distancia recorrida.
        • g es la aceleración originada por la gravedad es decir 9.8𝑚/s^2.
        • t es el tiempo transcurrido.
        
    Esta y otras afirmaciones le valieron a Galileo una amable invitación a beber la Cicuta,
    pero finalmente fue condonada su pena a cadena Perpetua.
    
    En honor al gran científico Galilei, se debe implementar una aplicación que dada una altura en metros de un edificio
    del que se va a lanzar una esfera, vaya mostrando la distancia recorrida segundo a segundo hasta tocar el suelo.
"""

height = float(input('Altura del edificio [m]: '))
g = 9.8
d = 0
t = 0
while d < height:
    print('Tiempo: %.2f s. Distancia recorrida: %.2f m.' % (t, d))
    t += 1
    d = (1/2) * g * t**2 # The initial velocity is assumed to be v = 0.
    
# Arrival of the object on the ground:
t_final = (2*height/g)**(1/2)
print('Tiempo: %.2f s. Distancia recorrida: %.2f m.' % (t_final, height))
