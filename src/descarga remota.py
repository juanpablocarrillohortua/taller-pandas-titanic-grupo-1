#descargue los csv automaticamente


import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


KAGGLE_DATASET_ID = f'titanic'  #extraido de la ruta web https://www.kaggle.com/competitions/titanic/data?select=train.csv
DOWNLOAD_PATH = '../data' #carpeta donde se descarga



def download_and_extract(dataset_id: str, path: str):

    try:
        # si la carpeta data no existe, creela
        if not os.path.exists(path):
            os.makedirs(path)
        
        print(f"Iniciando descarga del dataset: {dataset_id}")
        
        # 1. Autenticación y Descarga
        api = KaggleApi()
        api.authenticate()  #inicie secion en kaggle
        #necesario tener su api bien configurada en local (para mas detalle consulte el README de data)
        
        #descarge buscando el dataset con el id (para competencia)
        api.competition_download_files(dataset_id, path=path)

        
        print(f"Descarga completada. Archivos guardados en: {path}")
        
        # Descompresión 
        for item in os.listdir(path):

            if item.endswith('.zip'):

                file_path = os.path.join(path, item) #construya la ruta al zip descargado

                print(f"Descomprimiendo {item}...")

                with zipfile.ZipFile(file_path, 'r') as zipp: #asegure cierre automatico del zip y asigne el zip a la var zipp

                    zipp.extractall(path)
                
                # Eliminar el archivo .zip después de la descompresión
                os.remove(file_path)
                print(f"Archivo {item} descomprimido y eliminado.")
                
        print("\n¡Proceso de descarga y extracción finalizado con éxito!")

    except Exception as e:
        print(f"\nError durante el proceso: {e}")


# EJECUCIÓN


if __name__ == "__main__":
    download_and_extract(KAGGLE_DATASET_ID, DOWNLOAD_PATH)