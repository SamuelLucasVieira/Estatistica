import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Load import loads

# Caminho do arquivo CSV
CSV_FILE_PATH = r"C:\Users\LAB-56\Desktop\Estatistica\dados_A618_D_2022-10-01_2023-12-31.csv"

# Carregar os dados
dao = loads()
df = dao.load_csv(CSV_FILE_PATH)

# Lista para armazenar valores numéricos
valores = []

# Processamento dos valores da coluna "TEMPERATURA"
for row in df["TEMPERATURA"]:
    numero_str = re.sub(r"[^\d,]", "", row)  # Remover caracteres não numéricos
    numero_str = numero_str.replace(",", ".")  # Trocar vírgula por ponto para formato numérico
    try:
        numero_float = float(numero_str)
        valores.append(numero_float)
    except ValueError:
        continue  # Ignorar valores inválidos

# Análise estatística
if valores:
    valores_series = pd.Series(valores)
    
    # Cálculo das estatísticas básicas
    media = valores_series.mean()
    mediana = valores_series.median()
    moda = valores_series.mode().iloc[0] if not valores_series.mode().empty else None
    variancia = valores_series.var()
    desvio_padrao = valores_series.std()
    
    # Cálculo dos quartis
    q1 = valores_series.quantile(0.25)
    q2 = valores_series.quantile(0.50)  # Mediana
    q3 = valores_series.quantile(0.75)
    
    # Cálculo dos percentis 5 e 95
    p5 = valores_series.quantile(0.05)
    p95 = valores_series.quantile(0.95)
    
    # Identificação de outliers usando o IQR
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = valores_series[(valores_series < limite_inferior) | (valores_series > limite_superior)]

    # Criar um DataFrame com o relatório estatístico
    relatorio_df = pd.DataFrame({
        "Métrica": [
            "Média", "Mediana", "Moda", "Variância", "Desvio Padrão",
            "Q1 (25%)", "Q2 (50%) / Mediana", "Q3 (75%)",
            "P5 (5%)", "P95 (95%)",
            "Quantidade de Outliers"
        ],
        "Valor": [
            f"{media:.2f}", f"{mediana:.2f}", f"{moda:.2f}", f"{variancia:.2f}", f"{desvio_padrao:.2f}",
            f"{q1:.2f}", f"{q2:.2f}", f"{q3:.2f}",
            f"{p5:.2f}", f"{p95:.2f}",
            len(outliers)
        ]
    })

    # Criar e exibir o boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=valores_series)
    plt.title("Box Plot da Temperatura")
    plt.xlabel("Temperatura")
    plt.grid(True)
    plt.show()

    # Exibir relatório no terminal
    print("\n===== Relatório Estatístico da Temperatura =====\n")
    print(relatorio_df.to_string(index=False))

    # Salvar o relatório como arquivo de texto
    relatorio_df.to_csv("relatorio_temperatura.txt", sep="\t", index=False)
    print("\nRelatório salvo como 'relatorio_temperatura.txt'.")

    # Salvar o relatório como arquivo Excel
    relatorio_df.to_excel("relatorio_temperatura.xlsx", index=False)
    print("Relatório salvo como 'relatorio_temperatura.xlsx'.")

else:
    print("Nenhum valor válido encontrado na coluna TEMPERATURA.")
