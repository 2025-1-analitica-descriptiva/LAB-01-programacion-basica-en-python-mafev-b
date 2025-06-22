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

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = read_dataset("files/input/data.csv")
    results = {}
    for row in data:
        letter = row[0]
        value = int(row[1])
        if letter not in results:
            results[letter] = [value, value]
        else:
            if value > results[letter][0]:
                results[letter][0] = value
            if value < results[letter][1]:
                results[letter][1] = value
    final_result = []
    for letter in sorted(results.keys()):
        maximum, minimum = results[letter]
        final_result.append((letter, maximum, minimum))
    return final_result



