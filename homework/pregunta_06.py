"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def read_dataset(filepath):
    """
    Reads a tab-separated CSV file and returns a list of rows,
    where each row is a list of column values.
    """
    rows = []
    with open(filepath, "r") as file:
        for line in file:
            cols = line.strip().split("\t")
            rows.append(cols)
    return rows

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
    data = read_dataset("files/input/data.csv")
    key_values = {}

    for row in data:
        items = row[4].split(',')
        for item in items:
            key, value = item.split(':')
            value = int(value)
            if key not in key_values:
                key_values[key] = [value, value]
            else:
                if value < key_values[key][0]:
                    key_values[key][0] = value
                if value > key_values[key][1]:
                    key_values[key][1] = value

    result = [(key, key_values[key][0], key_values[key][1]) for key in sorted(key_values.keys())]
    return result

