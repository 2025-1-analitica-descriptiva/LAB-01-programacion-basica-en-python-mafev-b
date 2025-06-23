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
    data = read_dataset("files/input/data.csv")
    key_count = {}

    for row in data:
        items = row[4].split(',')
        for item in items:
            key = item.split(':')[0]
            key_count[key] = key_count.get(key, 0) + 1

    return dict(sorted(key_count.items()))

