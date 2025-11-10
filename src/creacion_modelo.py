import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier #importar el modelo desde sklearn
from sklearn.model_selection import cross_val_score #importar metodo de validación

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) ##acceder a la carpeta del script, ruta absoluta de la carpeta

data_dir = os.path.join(BASE_DIR, '..', 'data') ##suba un nivel y acceda a la carpeta data

test_path = os.path.join(data_dir, 'test.csv')
train_path = os.path.join(data_dir, 'train.csv')

df_test = pd.read_csv(test_path)
df_train = pd.read_csv(train_path)

TARGET_COL = 'Survived' #variable para rellenar

X_train = df_train.drop(columns=[TARGET_COL, "Ticket","PassengerId" , "Cabin", "Name"]) #eliminar col target y columnas poco representativas
X_train = pd.get_dummies(X_train, columns=['Sex', 'Embarked'], drop_first=True) #codificar variables str
# y_train es la columna objetivo
y_train = df_train[TARGET_COL]


X_test = df_test.drop(columns=["Ticket","PassengerId" , "Cabin", "Name"])
X_test = pd.get_dummies(X_test, columns=['Sex', 'Embarked'], drop_first=True) #codificar variables str

# 3. Crear y Entrenar el Modelo
rf_model = RandomForestClassifier(n_estimators=100, #numero de arboles
                                  random_state=42) #para replicar resultados

print("Entrenando el modelo...")
rf_model.fit(X_train, y_train) 
print("Entrenamiento completado.")

predictions = rf_model.predict(X_test)

#Predecir
predicciones = rf_model.predict(X_test)