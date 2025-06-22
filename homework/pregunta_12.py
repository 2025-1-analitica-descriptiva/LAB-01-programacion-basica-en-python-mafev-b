"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

 with open('./files/input/data.csv', 'r') as file:
        lines = file.readlines()
    result = {}
    for line in lines:
        columns = line.split()
        letter = columns[0]
        vals = columns[4].split(',')
        for val in vals:
            if letter in result:
                result[letter] += int(val.split(':')[1])
            else:
                result[letter] = int(val.split(':')[1])
    return result