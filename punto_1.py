"""El capitán del barco pirata Thousand Sunny, el famoso Monkey D. Luffy te ha designado
para que sirva de vigía en el mástil principal. Esto es lo que te ha dicho el capitán:
    
    Tu misión es simple marinero, pero importante para la tripulación,
    cuando veas alguna de estas criaturas debes decirlo de esta manera:
    
    •¡Ahoy! capitán, un Kraken
    •¡Ahoy! capitán, unas Sirenas
    •¡Ahoy! capitán, una Ballena
    •¡Ahoy! capitán, un Hipocampo
    •¡Ahoy! capitán, una Macaraprono
    •¡Ahoy! capitán, un Pulpo
    •¡Ahoy! capitán, unos Leviatanes
    •¡Ahoy! capitán, Unas Hidras
    
    Tu vida va en ello marinero, debes pronunciarlos con el articulo correcto
    de acuerdo con su especie (uno, una, unos, unas).
    
    Además, debes decirla dirección del barco por la que aparece la criatura:
    
    •A babor
    •A estribor
    •Por la proa
    •Por la popa
    
Para cumplir la misión debes crear un programa que, dada la criatura y la ubicación, construya la cadena
correcta. El programa se debe ejecutar las veces que sea necesario hasta que el capital te diga “stop”.

Por ejemplo, si aparecen:

•Kraken y Babor debe decir: ¡Ahoy! capitán, un Kraken a babor.
•Leviatanes y Proa debe decir: ¡Ahoy! capitán, unos Leviatanes por la proa.

Y así hasta que ingresen la palabra para detener el programa.
"""

creatures = ['Kraken', 'Sirenas', 'Ballena', 'Hipocampo', 'Macaraprono',
             'Pulpo', 'Leviatanes', 'Hidras']
locations = ['Babor', 'Estribor', 'Proa', 'Popa']

word = ''
while word != 'stop':

    creature = input('Criatura: ')
    if creature not in creatures:
        print('Criatura inválida.')
        continue
    else:
        location = input('Ubicación: ')
        if location not in locations:
            print('Ubicación inválida.')
            continue
        else:
            if creature == 'Kraken' or creature == 'Hipocampo' or creature == 'Pulpo':
                article_creature = 'un'
            elif creature == 'Sirenas' or creature == 'Hidras':
                article_creature = 'unas'
            elif creature == 'Ballena' or creature == 'Macaraprono':
                article_creature = 'una'
            else:
                article_creature = 'unos'
                
            if location == 'Babor' or location == 'Estribor':
                article_location = 'a'
            else:
                article_location = 'por la'
            
            print(f'¡Ahoy! capitán, {article_creature} {creature} {article_location} {location.lower()}.')
            
            word = input('El capitán dice: ')
        