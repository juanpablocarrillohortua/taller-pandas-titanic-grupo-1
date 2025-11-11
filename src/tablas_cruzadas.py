import pandas  as pd
from typing import Optional, List, Dict, Any, Literal


def cruzar_por_survived(data, col): ## cruza segun una culumna especifica y la supervivencia
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
    
def clasificar_edades_estandar(edad):
    if edad < 10:
        return 'Niño'
    elif 10 <= edad < 18:
        return 'Adolescente' 
    elif 18 <= edad <= 49:
        return 'Adulto'
    else:
        return 'Mayor'
    


def cruzar_por_survived_etaria(data:pd.DataFrame, gender: Optional[Literal['male', 'female']] = None, categoria: Optional[Literal['k_m', 'c_d']] = None):
    #cruce con clacificacion etaria 
    # categorias: 

    # k_m; kid vs man
    # c_d cincuenta vs diez

    #tambien da la posibilidad de discriminar el genero

    #discriminacion por genero
    if gender: 
        try:
            df_grouped = data[data['Sex'] == gender].copy()
        except Exception as e:
            raise ValueError('genero no existe')
    else:
        df_grouped = data.copy()

    if categoria == "k_m": #kid man, clacifique con criterio de mayoria de edad
        df_grouped['grupo etario'] = df_grouped['Age'].apply(lambda x: 'niño' if x < 18 else "hombre")

    elif categoria == "c_d": #clacifique con criterio de edades 50, 10 u otro
        df_grouped['grupo etario'] = df_grouped['Age'].apply(clasificar_edades)
    



    #arupamiento
    df_grouped = df_grouped.groupby(['grupo etario', 'Survived']).size().reset_index(name='Count') #conteo


    df_grouped['Supervivencia_Etiqueta'] = df_grouped['Survived'].apply(lambda x: 'Sí Sobrevivió' if x == 1 else 'No Sobrevivió') #etiqueta de supervivencia

    #porcentajes
    df_grouped['total por grupo'] = df_grouped.groupby('grupo etario')['Count'].transform('sum')
    df_grouped['Percent'] = (df_grouped['Count']/df_grouped['total por grupo'])*100

    #ajustar output
    if categoria == "k_m":
        df_hombre = df_grouped[df_grouped['grupo etario'] == 'hombre']
        df_nino = df_grouped[df_grouped['grupo etario'] == 'niño']
        return [df_grouped, df_hombre, df_nino]
    
    elif categoria == 'c_d':
        df_cincuenta = df_grouped[df_grouped['grupo etario'] == 'mayor a 50 años']
        df_diez = df_grouped[df_grouped['grupo etario'] == 'menor a 10 años']
        df_otro = df_grouped[df_grouped['grupo etario'] == 'ninguno de los grupos de interes']
        return [df_grouped, df_cincuenta, df_diez, df_otro]
    
    





def cruzar_ports_survived(data:pd.DataFrame, port_interest: Optional[Literal['S', 'C', 'Q']] = None, only_surv=True,  only_interest_port = False):
    #que puerto interesa
    match port_interest:
        case 'S':
            puertos = {"S": "Southampton", "C": "Otro", "Q":"Otro"}
        case 'C':
            puertos = {"S": "Otro", "C": "Cherbourg", "Q":"Otro"}
        case 'Q':
            puertos = {"S": "Otro", "C": "Otro", "Q":"Queenstown"}
        case _:
            puertos = {"S": "Southampton", "C": "Cherbourg", "Q":"Queenstown"}
    df_grouped = data.copy()

    #labeling segun interes
    df_grouped['Puerto de interes'] = df_grouped['Embarked'].map(puertos)

    df_grouped = df_grouped.groupby(['Puerto de interes', 'Survived']).size().reset_index(name="Conteo")
    df_grouped["Total puerto"] = df_grouped.groupby('Puerto de interes')["Conteo"].transform('sum')
    df_grouped['Percent'] = (df_grouped['Conteo']/df_grouped['Total puerto'])*100
    df_grouped['Supervivencia_Etiqueta'] = df_grouped['Survived'].apply(lambda x: 'Sí Sobrevivió' if x == 1 else 'No Sobrevivió')

    #ajustar output 
    #only_surv: solo muestra survived ==1
    #only_interest_port: solo muestra port == port_interest
    if only_surv:
        return df_grouped[df_grouped['Survived'] == 1]
    elif only_interest_port:
        return df_grouped[df_grouped['Puerto de interes'] == puertos[port_interest]]
    elif only_surv and only_interest_port:
        return df_grouped[(df_grouped['Puerto de interes'] == puertos[port_interest]) & (df_grouped['Survived'] == 1)]
    else:
        return df_grouped
    




def segun_cabina(data):
    def grupo_fam(cant):
        if cant == 0:
            return 'sin familiares a bordo (Grupo 1)'
        elif 1 <= cant <= 3:
            return 'familias pequeñas (Grupo 2)'
        elif cant >= 4:
            return 'familias grandes (Grupo 3)'

    def tipo_cabin(cab):
        tipos = ['A', 'B', 'C', 'D', 'E', 'F', 'N'] #N para Ninguna
        for i in tipos:
            if cab[0] == i:
                return i
    

    df_familias = data.copy()
    df_familias['Tipo familia'] = df_familias['Familiares'].apply(grupo_fam)
    df_familias['Tipo cabina'] = df_familias['Cabin'].apply(tipo_cabin)


    df_familias = df_familias.groupby(['Tipo cabina', 'Tipo familia']).size().reset_index(name='Count')
    df_familias['Total'] = df_familias.groupby('Tipo cabina')['Count'].transform('sum')
    df_familias['Percent'] = (df_familias['Count']/df_familias['Total']) * 100

    #se elimina los tipo N (ninguna cabina)
    df_familias = df_familias[df_familias['Tipo cabina'] != 'N']

    return df_familias