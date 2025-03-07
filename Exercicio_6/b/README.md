# Relatório Estatístico da Temperatura

Este documento explica o significado dos valores calculados na análise estatística da temperatura.

## 1. Média
A **média** representa o **valor médio** da temperatura ao longo do período analisado. Ela é calculada somando todos os valores da temperatura e dividindo pelo número total de observações.

### **Interpretação**:
- Se a média for **alta ou baixa**, pode indicar uma tendência climática.
- Se houver valores extremos (outliers), a média pode ser **distorcida**, por isso é importante considerar a **mediana** também.

## 2. Mediana
A **mediana** representa o **valor central** da distribuição. Ou seja, **50% dos dados estão abaixo dela e 50% acima**.

### **Interpretação**:
- A mediana é **menos sensível a outliers** do que a média.
- Se a média e a mediana forem **próximas**, significa que os dados estão **simetricamente distribuídos**.
- Se a média for **muito maior ou menor** que a mediana, significa que há valores extremos (outliers) que afetam a distribuição.

## 3. Moda
A **moda** é o valor que **mais se repete** na série de temperaturas.

### **Interpretação**:
- Se a moda for **diferente da média e da mediana**, pode indicar que há **valores muito comuns** na distribuição.
- Se houver **mais de uma moda**, significa que há **múltiplos valores mais frequentes** na série de dados.

## 4. Variância
A **variância** mede o **grau de dispersão dos dados** em relação à média. Ela mostra **o quanto os valores variam entre si**.

### **Interpretação**:
- **Valores altos de variância** → significam que as temperaturas flutuam bastante (muita variação).
- **Valores baixos de variância** → significam que as temperaturas são mais constantes.

## 5. Desvio Padrão
O **desvio padrão** é a raiz quadrada da variância e indica o **nível médio de variação** das temperaturas em relação à média.

### **Interpretação**:
- Um **desvio padrão alto** significa que os valores estão muito dispersos (ou seja, há uma grande variação nas temperaturas).
- Um **desvio padrão baixo** significa que os valores estão mais concentrados próximos da média.

## 6. Quartis (Q1, Q2, Q3)
Os **quartis** dividem os dados em **4 partes iguais**, ajudando a entender a distribuição das temperaturas:

- **Q1 (Primeiro Quartil - 25%)** → 25% dos dados estão **abaixo desse valor**.
- **Q2 (Mediana - 50%)** → 50% dos dados estão **abaixo desse valor**.
- **Q3 (Terceiro Quartil - 75%)** → 75% dos dados estão **abaixo desse valor**.

### **Interpretação**:
- Se a **diferença entre Q3 e Q1 for grande**, significa que há **muita variação nos dados**.
- O **Intervalo Interquartil (IQR = Q3 - Q1)** ajuda a identificar **outliers**.

## **Resumo Prático**
1. **Média** → Temperatura média do período.
2. **Mediana** → Valor central dos dados (50% acima e 50% abaixo).
3. **Moda** → Temperatura mais frequente.
4. **Variância** → Mede o grau de variação nos dados.
5. **Desvio Padrão** → Mede a dispersão em relação à média.
6. **Quartis** → Mostram a distribuição dos valores e ajudam a identificar outliers.

### **Conclusão**
Os valores calculados ajudam a entender como a temperatura variou ao longo do tempo. A média e a mediana indicam os valores centrais, enquanto a variância e o desvio padrão mostram o grau de dispersão. Os quartis fornecem informações sobre a distribuição dos dados, e a identificação de outliers ajuda a detectar valores anormais que podem indicar eventos climáticos extremos ou erros de medição.

