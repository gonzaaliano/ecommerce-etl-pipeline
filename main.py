from pathlib import Path
from etl.extract import load_datasets
from etl.transform import optimize_dataframe
from etl.analyze import analyze_dataframe
from etl.load import load_all

DATA_PATH = Path("data")

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("La carpeta data no existe")

    # 1. Extract
    datasets = load_datasets(DATA_PATH)

    # 2. Transform
    datasets = {
        name: optimize_dataframe(df)
        for name, df in datasets.items()
    }

    # 3. Analyze
    for df in datasets.values():
        analyze_dataframe(df)

    load_all(datasets, format="parquet")