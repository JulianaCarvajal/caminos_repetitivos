"""Dadas dos listas, se debe crear un programa que genere una tercera lista con los elementos
que se repiten en las dos anteriores listas sin repetirse ningún elemento en la nueva lista.
Lista 1: ['h', 'e', 'l', 'l', 'o', '', 't', 'e', 'a', 'm']
Lista 2: ['h', 'e', 'l', 'l', 'o', '','w', 'o', 'r', 'l', 'd']
"""

list_1 = ['h', 'e', 'l', 'l', 'o', '', 't', 'e', 'a', 'm']
list_2 = ['h', 'e', 'l', 'l', 'o', '','w', 'o', 'r', 'l', 'd']

list_3 = []

for i in list_1:
    if i in list_2 and i not in list_3:
        list_3.append(i)
        
print(list_3)
