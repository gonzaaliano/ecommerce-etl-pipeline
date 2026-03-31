from pathlib import Path
from etl.extract import load_datasets
from etl.transform import optimize_dataframe, transform_customers, transform_inventory, transform_orders, transform_products, transform_promotions, transform_reviews, transform_categories
from etl.load import save_dataframe_as_csv, save_dataframe_as_parquet

DATA_PATH = Path("data")

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("La carpeta data no existe")

    # 1. Extract
    datasets = load_datasets(DATA_PATH)
    

    # 2. Optimize
    for file_name, df in datasets.items():
        datasets[file_name] = optimize_dataframe(df, name = file_name)

    # 3. Transform
    datasets["ecommerce_categories"] = transform_categories(datasets["ecommerce_categories"])
    datasets["ecommerce_customers"] = transform_customers(datasets["ecommerce_customers"])
    datasets["ecommerce_inventory"] = transform_inventory(datasets["ecommerce_inventory"])
    datasets["ecommerce_orders"] = transform_orders(datasets["ecommerce_orders"])
    datasets["ecommerce_products"] = transform_products(datasets["ecommerce_products"])
    datasets["ecommerce_promotions"] = transform_promotions(datasets["ecommerce_promotions"])
    datasets["ecommerce_reviews"] = transform_reviews(datasets["ecommerce_reviews"])
    
    # 4. Load
    for name, df in datasets.items():
        save_dataframe_as_csv(df, name)
        save_dataframe_as_parquet(df, name)

if __name__ == "__main__":
    main()