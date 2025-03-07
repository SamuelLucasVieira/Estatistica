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

# Calcular os percentis 5 e 95
if valores:
    valores_series = pd.Series(valores)
    p5 = valores_series.quantile(0.05)   # Percentil 5%
    p95 = valores_series.quantile(0.95)  # Percentil 95%

    print(f"Percentil 5 (P5): {p5:.2f}")
    print(f"Percentil 95 (P95): {p95:.2f}")
else:
    print("Nenhum valor válido encontrado na coluna TEMPERATURA.")
