import pandas  as pd
from typing import Optional, List, Dict, Any, Literal


def cruzar_por_survived(data, col):
    df_grouped = data.groupby([col, 'Survived']).size().reset_index(name='Count')
    df_grouped['Supervivencia_Etiqueta'] = df_grouped['Survived'].apply(lambda x: 'Sí Sobrevivió' if x == 1 else 'No Sobrevivió')
    df_grouped['Total_by_col'] = df_grouped.groupby(col)['Count'].transform('sum') ##aplicar la suma del total de cada genero a las filas de ese genero
    df_grouped['Percentage'] = (df_grouped['Count'] / df_grouped['Total_by_col']) * 100 
    return df_grouped

def clasificar_edades(edad):
    if edad < 10:
        return "menor a 10 años"
    elif edad > 50:
        return "mayor a 50 años"
    else:
        return 'ninguno de los grupos de interes'


def cruzar_por_survived_etaria(data:pd.DataFrame, gender: Optional[Literal['male', 'female']] = None, categoria: Optional[Literal['k_m', 'c_d']] = None):
    if gender:
        try:
            df_grouped = data[data['Sex'] == gender].copy()
        except Exception as e:
            raise ValueError('genero no existe')
    else:
        df_grouped = data.copy()
        
    if categoria == "k_m": #kid man
        df_grouped['grupo etario'] = df_grouped['Age'].apply(lambda x: 'niño' if x < 18 else "hombre")
    elif categoria == "c_d": #cincuenton 10
        df_grouped['grupo etario'] = df_grouped['Age'].apply(clasificar_edades)

    df_grouped = df_grouped.groupby(['grupo etario', 'Survived']).size().reset_index(name='Count')
    df_grouped['Supervivencia_Etiqueta'] = df_grouped['Survived'].apply(lambda x: 'Sí Sobrevivió' if x == 1 else 'No Sobrevivió')
    df_grouped['total por grupo'] = df_grouped.groupby('grupo etario')['Count'].transform('sum')
    df_grouped['Percent'] = (df_grouped['Count']/df_grouped['total por grupo'])*100
    if categoria == "k_m":
        df_hombre = df_grouped[df_grouped['grupo etario'] == 'hombre']
        df_nino = df_grouped[df_grouped['grupo etario'] == 'niño']
        return [df_grouped, df_hombre, df_nino]
    else:
        df_cincuenta = df_grouped[df_grouped['grupo etario'] == 'mayor a 50 años']
        df_diez = df_grouped[df_grouped['grupo etario'] == 'menor a 10 años']
        df_otro = df_grouped[df_grouped['grupo etario'] == 'ninguno de los grupos de interes']
        return [df_grouped, df_cincuenta, df_diez, df_otro]