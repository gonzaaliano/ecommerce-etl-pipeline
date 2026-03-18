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

#En lugar de leer cada archivo individualmente, creamos un diccionario y leemos todos los archivos.
#glob.csv lee todos los archivos .csv contenidos en la carpeta data
for file in csv_files:
    df = pd.read_csv(file)
    df = optimize_dataframe(df)
    datasets[file.stem] = df

#file.stem devuelve el nombre del archivo sin la extensión .csv
# print(datasets.keys())
# for name, df in datasets.items():
#     print(f"{name}: {df.shape}")
#     print(f"\n📈 RESUMEN:")
#     print(f'INFO')
#     print(f'{df.info()}')
#     print(f'HEAD') 
#     print(f'{df.head()}')
#     print(f'DESCRIBE')
#     print(f'{df.describe()}')

# brands = datasets['ecommerce_brands']
# print(brands.head(15))
# print(brands.info())
# print(brands.describe())
# print(brands.isnull().sum())

# categories = datasets['ecommerce_categories']
# print(categories.head(10))
# print(categories.info())
# print(categories.describe())

#Detectamos valores nulos en el campo parent_category_id (Entendemos que son raíces del árbol de categorías)
# print(categories.isnull().sum())
# null_parent_category_id = categories['parent_category_id'].isnull().sum()
# print(f"SUMATORIA ID PADRE NULL EN CATEGORÍA {null_parent_category_id}")

# customers = datasets['ecommerce_customers']
# print(customers.head())
# print(customers.info())
# print(customers.describe())

#NO SE DETECTARON VALORES NULL EN CUSTOMERS DF
# print(customers.isnull().sum())

# inventory = datasets['ecommerce_inventory']
# print(inventory.head())
# print(inventory.info())
# print(inventory.describe())

# #NO SE DETECTARON VALORES NULL EN CUSTOMERS DF
# print(inventory.isnull().sum())

# order_items = datasets['ecommerce_order_items']
# print(order_items.info())
# print(order_items.head())
# print(order_items.describe())
# # #NO SE DETECTARON VALORES NULL EN ORDER_ITEMS DF
# print(order_items.isnull().sum())

# orders = datasets['ecommerce_orders']
# print(orders.info())
# print(orders.head())
# print(orders.describe())
# #SE DETECTARON VALORES NULL EN CAMPO PROMOTION_ID Y NOTES, LO QUE PODRÍA INDICAR UNA COMPRA SIN PROMOCIÓN, O QUE LA PROMOCIÓN NO SE APLICÓ.
# print(orders.isnull().sum())

# products = datasets['ecommerce_products']
# print(products.head())
# print(products.info())
# print(products.describe())
#NO SE DETECTARON VALORES NULL EN ORDER_ITEMS DF
# print(products.isnull().sum())

# promotions = datasets['ecommerce_promotions']
# print(promotions.head())
# print(promotions.info())
# print(promotions.describe())

reviews = datasets['ecommerce_reviews']
print(reviews.head())
print(reviews.info())
print(reviews.describe())

suppliers = datasets['ecommerce_suppliers']
print(suppliers.head())
print(suppliers.info())
print(suppliers.describe())

warehouses = datasets['ecommerce_warehouses'] 
print(warehouses.head())
print(warehouses.info())
print(warehouses.describe())



