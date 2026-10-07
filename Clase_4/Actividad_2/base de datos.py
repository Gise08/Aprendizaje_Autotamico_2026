import seaborn as sns
import pandas as pd

# Carga directa del dataset real oficial de Seaborn
df_real = sns.load_dataset('mpg')

# Renombramos las columnas al español
df_real = df_real.rename(columns={
    'mpg': 'rendimiento_mpg',
    'cylinders': 'cilindros',
    'displacement': 'cilindrada',
    'horsepower': 'potencia_hp',
    'weight': 'peso_libras',
    'acceleration': 'aceleracion',
    'model_year': 'anio_modelo',
    'origin': 'origen',
    'name': 'nombre_vehiculo'
})

# Guardamos el archivo CSV físico en tu subcarpeta Actividad_1
df_real.to_csv("rendimiento_vehiculos.csv", index=False)
print("¡Archivo 'rendimiento_vehiculos.csv' guardado exitosamente!")
display(df_real.head())