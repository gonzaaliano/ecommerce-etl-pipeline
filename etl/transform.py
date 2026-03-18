import pandas as pd

#Método para otimizar dataframe, intenta usar el tipo de dato mas chico posible sin romper los datos. Optimización de memoria entre 50%-80%
def optimize_dataframe(dataframe):
    for col in dataframe.select_dtypes(include=["int"]):
        dataframe[col] = pd.to_numeric(dataframe[col], downcast="integer")

    for col in dataframe.select_dtypes(include=["float"]):
        dataframe[col] = pd.to_numeric(dataframe[col], downcast="float")

    #OPTIMIZACIÓN DE COLUMNAS DE TIPO OBJETO A CATEGÓRICO SI TIENEN MENOS DE 50% DE VALORES ÚNICOS (CARDINALIDAD)
    for col in dataframe.select_dtypes(include=["object"]):
        if dataframe[col].nunique() / len(dataframe[col]) < 0.5:
            dataframe[col] = dataframe[col].astype("category")

    return dataframe