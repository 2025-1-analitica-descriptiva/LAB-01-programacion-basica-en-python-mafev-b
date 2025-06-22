"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

with open('./files/input/data.csv', 'r') as file:
        lines = file.readlines()

    counts = {}

    for line in lines:
        columns = line.split()
        dictionary_str = columns[4]
        dictionary_items = dictionary_str.split(',')

        for item in dictionary_items:
            key, value = item.split(':')
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    return counts