import pandas as pd
from pathlib import Path

#Parametro de tipo Path, devolución de lista de tipo Path
def get_csv_files(data_Path: Path) -> list[Path]:
    csv_files = list(data_Path.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data directory")

    return csv_files

def read_csv_files():
    pass
    

#Método para otimizar dataframe, intenta usar el tipo de dato mas chico posible sin romper los datos. Optimización de memoria entre 50%-80%
def optimize_dataframe(dataframe):
    for col in dataframe.select_dtypes(include=["int"]):
        dataframe[col] = pd.to_numeric(dataframe[col], downcast="integer")

    for col in dataframe.select_dtypes(include=["float"]):
        dataframe[col] = pd.to_numeric(dataframe[col], downcast="float")

    for col in dataframe.select_dtypes(include=["object"]):
        dataframe[col] = pd.to_numeric(dataframe[col], downcast="category")

    return dataframe
