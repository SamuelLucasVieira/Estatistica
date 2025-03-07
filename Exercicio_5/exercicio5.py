import re
import pandas as pd
from Load import loads

CSV_FILE_PATH = r"C:\Users\LAB-56\Desktop\dados_A618_D_2022-10-01_2023-12-31.csv"

dao = loads()
df = dao.load_csv(CSV_FILE_PATH)

# Lista para armazenar valores numéricos
valores = []

# Processamento dos valores da coluna "TEMPERATURA"
for row in df["TEMPERATURA"]:
    numero_str = re.sub(r"[^\d,]", "", row)
    numero_str = numero_str.replace(",", ".")
    try:
        numero_float = float(numero_str)
        valores.append(numero_float)
    except ValueError:
        continue  # Ignorar valores inválidos

# Identificar outliers
if valores:
    valores_series = pd.Series(valores)
    
    # Cálculo dos quartis e IQR
    q1 = valores_series.quantile(0.25)  # Primeiro quartil (Q1)
    q3 = valores_series.quantile(0.75)  # Terceiro quartil (Q3)
    iqr = q3 - q1  # Intervalo interquartil (IQR)
    
    # Limites para outliers
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    # Filtrando os outliers
    outliers = valores_series[(valores_series < limite_inferior) | (valores_series > limite_superior)]

    # Exibir resultados
    if not outliers.empty:
        print("Outliers encontrados:")
        print(outliers.to_list())
    else:
        print("Nenhum outlier encontrado nos dados.")
else:
    print("Nenhum valor válido encontrado na coluna TEMPERATURA.")
