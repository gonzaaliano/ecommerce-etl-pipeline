from pathlib import Path
from etl.extract import load_datasets
from etl.transform import optimize_dataframe
from etl.analyze import analyze_all

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
    analyze_all(datasets)


if __name__ == "__main__":
    main()