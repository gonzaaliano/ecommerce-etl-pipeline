from pathlib import Path
from etl.extract import load_datasets
from etl.transform import optimize_dataframe

#Define la carpeta en donde se encuentran los archivos
DATA_PATH = Path('data')

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("La carpeta data no existe")

    datasets = load_datasets(DATA_PATH)

    for name, df in datasets.items():
        df = optimize_dataframe(df)
        print(f"{name}: {df.shape}")
        print(f"\n📈 RESUMEN:")
        print(f'INFO')
        print(f'{df.info()}')
        print(f'HEAD') 
        print(f'{df.head()}')
        print(f'DESCRIBE')
        print(f'{df.describe()}')