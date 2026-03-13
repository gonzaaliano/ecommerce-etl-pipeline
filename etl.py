import pandas as pd
from pathlib import Path

#Define la carpeta en donde se encuentran los archivos
DATA_PATH = Path('data')
datasets = {}

if not DATA_PATH.exists():
    raise FileNotFoundError("La carpeta data no existe")

csv_files = list(DATA_PATH.glob("*.csv"))

if not csv_files:
    raise ValueError('No hay archivos de tipo .csv en la carpeta data')

#Método para otimizar dataframe, intenta usar el tipo de dato mas chico posible sin romper los datos. Optimización de memoria entre 50%-80%
def optimize_dataframe(df):

    for col in df.select_dtypes(include=["int"]):
        df[col] = pd.to_numeric(df[col], downcast="integer")

    for col in df.select_dtypes(include=["float"]):
        df[col] = pd.to_numeric(df[col], downcast="float")

    for col in df.select_dtypes(include=["object"]):
        if df[col].nunique() / len(df[col]) < 0.5:
            df[col] = df[col].astype("category")

    return df

#En lugar de leer cada archivo individualmente, creamos un diccionario y leemos todos los archivos.
#glob.csv lee todos los archivos .csv contenidos en la carpeta data
for file in csv_files:
    df = pd.read_csv(file)
    df.info(memory_usage="deep")
    df = optimize_dataframe(df)
    df.info(memory_usage="deep")
    datasets[file.stem] = df

#file.stem devuelve el nombre del archivo sin la extensión .csv
# print(datasets.keys())
for name, df in datasets.items():
    print(f"{name}: {df.shape}")

brands = datasets['ecommerce_brands']
# print(brands.head())
# print(brands.info())
# print(brands.describe())

categories = datasets['ecommerce_categories']
# print(categories.head())
# print(categories.info())
# print(categories.describe())

customers = datasets['ecommerce_customers']
# print(customers.head())
# print(customers.info())
# print(customers.describe())

# inventory = datasets['ecommerce_inventory']
# order_items = datasets['ecommerce_order_items']
# orders = datasets['ecommerce_orders']
# products = datasets['ecommerce_products']
# promotions = datasets['ecommerce_promotions']
# reviews = datasets['ecommerce_reviews']
# suppliers = datasets['ecommerce_suppliers']
# warehouses = datasets['ecommerce_warehouses']



