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

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    data = read_dataset("files/input/data.csv")
    value_letters = {}

    for row in data:
        letter = row[0]
        value = int(row[1])
        if value not in value_letters:
            value_letters[value] = set()
        value_letters[value].add(letter)

    result = [(value, sorted(list(value_letters[value]))) for value in sorted(value_letters.keys())]
    return result

