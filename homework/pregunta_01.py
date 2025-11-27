"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import pandas as pd
import os
def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Leer los datos del archivo CSV
    df = pd.read_csv("files/input/news.csv")

    # Eliminar columna innecesaria si existe
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Sumar cada categoria (son columnas)
    category_counts = df.sum()

    # Crear directorio si no existe
    os.makedirs("files/plots", exist_ok=True)

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    category_counts.plot(kind='bar')
    plt.title('Cantidad de Noticias por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Cantidad de Noticias')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la gráfica
    plt.savefig("files/plots/news.png")
    plt.close()