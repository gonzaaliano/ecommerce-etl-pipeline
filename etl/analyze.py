#df.shape() Muestra tamaño del dataframe
#df.head() Muestra por defecto las 5 primeras filas. Si le pasas por parámetro un número te va a mostrar esa cantidad de filas.
#df.tail() Muestra por defecto las 5 últimas filas
import pandas as pd

def analyze_dataframe(name: str, df: pd.DataFrame) -> None:
    print(f"Nombre Dataset: {name}")
    print(f"Tamaño del dataframe: {df.shape}")
    print(f"\n📈 RESUMEN:")
    print(f'INFO')
    print(f'{df.info()}')
    print(f'HEAD')
    print(f'{df.head()}')
    print(f'DESCRIBE')
    print(f'{df.describe()}')
    print(f'VALORES NULOS')
    print(f'{df.isnull().sum()}')
    print(f"VALORES DUPLICADOS")
    print(f'{df.duplicated().sum()}')