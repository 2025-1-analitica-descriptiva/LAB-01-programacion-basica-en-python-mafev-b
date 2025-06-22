"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

with open('./files/input/data.csv', 'r') as file:
        lines = file.readlines()

    max_min_values = {}

    for line in lines:
        columns = line.split()
        letter = columns[0]
        value = int(columns[1])
        if letter in max_min_values:
            max_min_values[letter][0] = max(max_min_values[letter][0], value)
            max_min_values[letter][1] = min(max_min_values[letter][1], value)
        else:
            max_min_values[letter] = [value, value]

    result = [(letter, values[0], values[1]) for letter, values in max_min_values.items()]
    result.sort()

    return result