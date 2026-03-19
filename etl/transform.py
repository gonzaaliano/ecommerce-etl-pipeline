import pandas as pd

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = optimize_dataframe(df)
    df = handle_nulls(df)
    df = handle_duplicates(df)

    return df

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

#Método para buscar valores duplicados en un dataframe, devuelve la cantidad de valores duplicados por columna
def search_for_duplicates(dataframe):
    return dataframe.duplicated().sum()

def handle_duplicates(df: pd.DataFrame, threshold: float = 0.05):

    total_duplicates = df.duplicated().sum()
    ratio = total_duplicates / len(df)

    if total_duplicates == 0:
        print("✔ No duplicates")
        return df

    if ratio < threshold:
        df = df.drop_duplicates()
        print(f"✔ Duplicates removed ({total_duplicates})")
    else:
        print(f"⚠ Too many duplicates ({ratio:.2%}), not removed")

    return df

#Método para buscar valores nulos en un dataframe, devuelve la cantidad de valores nulos por columna
def search_for_null_values(dataframe):

    return dataframe.isnull().sum()

def handle_nulls(df: pd.DataFrame, threshold: float = 0.05) -> pd.DataFrame:
    """
    Si el porcentaje de nulos en una columna es menor al threshold,
    los reemplaza por 0. Si es mayor, no hace nada.
    """
    for col in df.columns:
        null_ratio = df[col].isnull().sum() / len(df)

        if null_ratio == 0:
            continue

        if null_ratio < threshold:
            df[col] = df[col].fillna(0)
            print(f"✔ {col}: nulos reemplazados ({null_ratio:.2%})")

        else:
            print(f"⚠ {col}: demasiados nulos ({null_ratio:.2%}), no se modifica")

    return df

def analyze_all(datasets: dict[str, pd.DataFrame]) -> None:

    for name, df in datasets.items():
        print(f"\nDataset: {name}")
        print("Nulls:")
        print(search_for_null_values(df))

    for name, df in datasets.items():
        print(f"\nDataset: {name}")
        print("Duplicates:")
        print(search_for_duplicates(df))