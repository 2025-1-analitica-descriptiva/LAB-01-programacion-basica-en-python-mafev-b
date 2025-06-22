"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

 with open('./files/input/data.csv', 'r') as file:
        lines = file.readlines()

    min_max_values = {}

    for line in lines:
        columns = line.split()
        dictionary_str = columns[4]
        dictionary_items = dictionary_str.split(',')

        for item in dictionary_items:
            key, value = item.split(':')
            value = int(value)

            if key in min_max_values:
                min_max_values[key][0] = min(min_max_values[key][0], value)
                min_max_values[key][1] = max(min_max_values[key][1], value)
            else:
                min_max_values[key] = [value, value]

    result = [(key, values[0], values[1]) for key, values in min_max_values.items()]
    result.sort()

    return result