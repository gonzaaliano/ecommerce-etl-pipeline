import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path("output")

def save_dataframe_as_csv(df: pd.DataFrame, name: str) -> None:
    OUTPUT_PATH.mkdir(exist_ok=True)
    file_path = OUTPUT_PATH / f"{name}_clean.csv"
    df.to_csv(file_path, index=False)
    print(f"✔ {name} saved to {file_path} as CSV file.")

def save_dataframe_as_parquet(df: pd.DataFrame, name: str) -> None:
    OUTPUT_PATH.mkdir(exist_ok=True)
    file_path = OUTPUT_PATH / f"{name}_clean.parquet"
    df.to_parquet(file_path, index=False)
    print(f"✔ {name} saved to {file_path} as Parquet file.")

def load_all(datasets: dict[str, pd.DataFrame], format: str = "parquet") -> None:
    for name, df in datasets.items():
        if format == "parquet":
            save_dataframe_as_parquet(df, name)
        elif format == "csv":
            save_dataframe_as_csv(df, name)