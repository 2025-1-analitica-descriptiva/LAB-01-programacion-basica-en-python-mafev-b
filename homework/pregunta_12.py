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

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data = read_dataset("files/input/data.csv")
    sums = {}

    for row in data:
        letra = row[0]
        items = row[4].split(',')
        suma = sum(int(item.split(':')[1]) for item in items)
        sums[letra] = sums.get(letra, 0) + suma

    # Retornar el diccionario ordenado por las letras
    return dict(sorted(sums.items()))

