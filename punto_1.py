"""Report sightings of creatures and the direction
of the ship from which they appear, correctly.

Do this until the captain says "stop".
"""

#import random

creatures = ['Kraken', 'Sirenas', 'Ballena', 'Hipocampo', 'Macaraprono',
             'Pulpo', 'Leviatanes', 'Hidras']
locations = ['Babor', 'Estribor', 'Proa', 'Popa']

word = ''
while word != 'stop':
    #creature = creatures[random.randint(0, len(creatures) - 1)]
    #location = locations[random.randint(0, len(locations) - 1)]
    
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
        