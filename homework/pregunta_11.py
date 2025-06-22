"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

with open('./files/input/data.csv', 'r') as file:
        lines = file.readlines()
    sums = {}
    for line in lines:
        columns = line.split()
        letters = columns[3].split(',')
        value = int(columns[1])
        for letter in letters:
            if letter in sums:
                sums[letter] += value
            else:
                sums[letter] = value
    sorted_sums = dict(sorted(sums.items()))
    return sorted_sums