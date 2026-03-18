# ETL - Extract SOLO LEER DATASETS

import pandas as pd
from pathlib import Path

#Parametro de tipo Path, devolución de lista de tipo Path. Formato de función en type hints
#Parametro 1 data_Path: Path -> El tipo de dato que se espera como argumento es un objeto de tipo Path
#Parametro 2 -> Lo que devuelve la función. En este caso una lista de objetos de tipo Path
def get_csv_files(data_Path: Path) -> list[Path]:
    csv_files = list(data_Path.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data directory")

    return csv_files

#Leer archivos CSV, con el parámetro de tipo Path, devuelve un DataFrame de pandas
def read_csv_files(file_path:Path) -> pd.DataFrame:
    return pd.read_csv(file_path, low_memory=False)

def load_datasets(data_path: Path) -> dict[str, pd.DataFrame]:
    datasets: dict[str, pd.DataFrame] = {}

    csv_files = get_csv_files(data_path)

    for file in csv_files:
        df = read_csv_files(file)
        datasets[file.stem] = df

    return datasets