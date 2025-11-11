import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def bar(x, y, color, title, data):
    fig = px.bar(
        data,
        x=x,                   # Eje X: grupo etario
        y=y,                 # Eje Y: Número de personas
        color=color, 
        barmode='group',           
        title=title,
        color_discrete_map={       
            'Sí Sobrevivió': 'green',
            'No Sobrevivió': 'red'
        }
    )
    fig.show()


def pie(n_pies, datas , col, titles):
    if n_pies == 2:
        fig, axes = plt.subplots(1, 2, figsize=(10, 5)) #lienzo de 1 fila y 2 columnas
    if n_pies == 3:
        fig, axes = plt.subplots(1, 3, figsize=(10, 5)) #lienzo de 1 fila y 3 columnas

    plt.style.use('seaborn-v0_8-whitegrid') 

    colores = ['red', 'green'] # Rojo para No Sobrevivió (0) y Verde para Sí Sobrevivió (1)

    # creacion primer grafico 
    axes[0].pie(
        datas[0][col],
        labels=datas[0]['Supervivencia_Etiqueta'],
        autopct='%1.1f%%', # Muestra el porcentaje con un decimal
        startangle=90,
        colors=colores
    )

    axes[0].set_title(titles[0])
    axes[0].axis('equal') # Asegura que el pastel sea un círculo

    #dibujar segunda col
    axes[1].pie(
        datas[1][col],
        labels=datas[1]['Supervivencia_Etiqueta'],
        autopct='%1.1f%%',      
        startangle=90,
        colors=colores
    )
    axes[1].set_title(titles[1])
    axes[1].axis('equal')

    if n_pies == 3:
        #dibujar tercera col
        axes[2].pie(
            datas[2][col],
            labels=datas[2]['Supervivencia_Etiqueta'],
            autopct='%1.1f%%',      
            startangle=90,
            colors=colores
        )
        axes[2].set_title(titles[2])
        axes[2].axis('equal')


    # 3. Ajustar el layout y mostrar
    plt.suptitle('Comparación de Supervivencia por Grupo Etario') # Título principal
    plt.tight_layout()
    plt.show()