import os
import sys

def obtener_rutas():
    BASE_DIR = os.getcwd() ##acceder a la carpeta del notebook, ruta absoluta de la carpeta

    csv_dir = os.path.join(BASE_DIR, '..', 'outputs', 'tablas') ##suba un nivel y acceda a la carpeta data
    graph_dir = os.path.join(BASE_DIR, '..', 'outputs', 'graficos')
    scr_dir = os.path.join(BASE_DIR, '..', 'src')
    sys.path.insert(0, scr_dir)

    return [csv_dir, graph_dir, scr_dir]

def exportar_tabla(data, name):
    rutas = obtener_rutas()
    df_path = os.path.join(rutas[0], name+".csv")  #cree la ruta del archivo

    if not os.path.exists(df_path):  #revise existencia del archivo

        print(f"Exportando tabla a: {rutas[0]}")
        data.to_csv(df_path, index=False, encoding='utf-8')
        print("Exportación de tabla completada.")
    else:
        print(f"El archivo '{name}.csv' ya existe en {rutas[0]}. No se exportó.")
    
def exportar_grafica(figure,name):
    rutas = obtener_rutas()

    graph_path = os.path.join(rutas[1], name + ".png")

    if not os.path.exists(graph_path):
        print(f"Exportando gráfico a: {rutas[1]}")

        figure.savefig(graph_path, dpi=300, bbox_inches='tight') 
        print("Exportación de gráfico completada.")
    else:
        print(f"El archivo '{name}.png' ya existe en {rutas[1]}. No se exportó.")
