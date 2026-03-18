import pandas as pd

def analyze_dataframe(name: str, df: pd.DataFrame) -> None:
    print(f"DATASET: {name}")
    print(f"SHAPE: {df.shape}")
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