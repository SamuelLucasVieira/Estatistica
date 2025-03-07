import re
import pandas as pd
from Load import loads

CSV_FILE_PATH = r"C:\Users\LAB-56\Desktop\Estatistica\dados_A618_D_2022-10-01_2023-12-31.csv"

dao = loads()
df = dao.load_csv(CSV_FILE_PATH)

# Contador para verificar o número de linhas processadas
num_rows = 0
valores = []

# Processamento dos valores da coluna "TEMPERATURA"
for row in df["TEMPERATURA"]:
    numero_str = re.sub(r"[^\d,]", "", row)
    numero_str = numero_str.replace(",", ".")
    try:
        numero_float = float(numero_str)
        valores.append(numero_float)
        num_rows += 1
    except ValueError:
        continue  # Ignorar valores inválidos

# Calcular estatísticas básicas
if valores:
    media = sum(valores) / num_rows
    mediana = pd.Series(valores).median()
    moda = pd.Series(valores).mode()
    
    # Pegar apenas um valor da moda (o primeiro, caso haja múltiplos)
    moda_unica = moda.iloc[0] if not moda.empty else None
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda_unica:.2f}")
else:
    print("Nenhum valor válido encontrado na coluna TEMPERATURA.")
