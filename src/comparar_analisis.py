import pandas as pd

df_test = pd.read_csv("../data/test.csv")
df_train = pd.read_csv("../data/train.csv")
columnas = df_train.columns   #se usa el de todas las col

#función cuyo funcionamiento se basa en tomar como arguemento las 2 bases de datos, las columnas como iterable, y el nombre de las bases(opcional)
#genera una descripción para cada uno de las bases de datos, y las concatena con pd.concat para lograr un output mas agradable de leer.
#adicionalmente si una columna no es compartida la salta y dice que no la encontró.

def analizar(data1, data2, cols,nombre_base1=None, nombre_base2=None):
    for col in cols:
        try:
            desc1=data1[col].describe()
            desc2=data2[col].describe()
            if nombre_base1 and nombre_base2:
                resultado_final = pd.concat([desc1, desc2], axis=1, keys=[nombre_base1, nombre_base2])
            else:
                resultado_final = pd.concat([desc1, desc2], axis=1, keys=['DF_A', 'DF_B'])
            print(f"columna: {col}")
            print(resultado_final)
            print("\n\n\n")
        except Exception as e:
            print(f"columna no {col} esta\n\n\n")

analizar(df_test, df_train, columnas, nombre_base1="test", nombre_base2="train")