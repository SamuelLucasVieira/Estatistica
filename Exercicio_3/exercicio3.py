import re
import pandas as pd
from Load import loads

CSV_FILE_PATH = r"C:\Users\LAB-56\Desktop\Estatistica\dados_A618_D_2022-10-01_2023-12-31.csv"

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

# Calcular os quartis
if valores:
    valores_series = pd.Series(valores)
    q1 = valores_series.quantile(0.25)  # Primeiro quartil (25%)
    q2 = valores_series.quantile(0.50)  # Segundo quartil (mediana, 50%)
    q3 = valores_series.quantile(0.75)  # Terceiro quartil (75%)

    print(f"Primeiro Quartil (Q1): {q1:.2f}")
    print(f"Segundo Quartil (Q2 / Mediana): {q2:.2f}")
    print(f"Terceiro Quartil (Q3): {q3:.2f}")
else:
    print("Nenhum valor válido encontrado na coluna TEMPERATURA.")
