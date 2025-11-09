import pandas as pd
import os
from scipy.stats import shapiro #test normalidad

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) ##acceder a la carpeta del script, ruta absoluta de la carpeta

data_dir = os.path.join(BASE_DIR, '..', 'data') ##suba un nivel y acceda a la carpeta data

test_path = os.path.join(data_dir, 'test.csv')
train_path = os.path.join(data_dir, 'train.csv')

df_test = pd.read_csv(test_path)
df_train = pd.read_csv(train_path)
columnas = df_train.columns   #se usa el de todas las col

#funcionamiento:
#se basa en el test de shapiro para seleccional un metodo de llenar los valores nulos. 
# si la variable es normal llena con la media
# si la variable NO es normal llena con la mediana

#Modo de uso:
#Pase la base de datos y columna de esta, se redefine la columna en base a la serie que devuelve la función
def limpieza_datos_numericos(df,col):
    stat, p = shapiro(df[col].dropna())
    if p<=0.05:
        print("La variable no sigue una distribución normal.")
        print("Se completan los datos nulos con la mediana.")
        a=df[col].fillna(df[col].median())
        return  a
    else:
        print("La variable sigue una distribución normal.")
        print("Se completan los datos nulos con la media.")
        a=df[col].fillna(df[col].mean())
        return a