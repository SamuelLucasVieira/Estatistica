# Guia de Execução - Análise Estatística da Temperatura

Este documento fornece instruções sobre como configurar um ambiente virtual, instalar as dependências e executar o código para análise estatística da temperatura.

## 📌 Requisitos
Antes de executar o código, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x**
- **Virtual Environment (venv)**
- **Arquivo CSV contendo os dados de temperatura**

## Clonando o Repositório e Configurando o Remoto

Para clonar este repositório e configurar o remoto, execute os seguintes comandos:

```bash
    git clone https://githu
    b.com/SamuelLucasVieira/Estatistica.git
    cd Estatistica
``` 
## 🚀 Como Configurar e Executar

1. **Criar um ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o script Python**:
   ```bash
   python analise_temperatura.py
   ```

## 📂 Estrutura de Arquivos

Após a execução, os seguintes arquivos serão gerados:

```
📁 Projeto/
│-- 📄 analise_temperatura.py  # Script principal
│-- 📄 requirements.txt  # Lista de dependências
│-- 📄 relatorio_temperatura.txt  # Relatório em texto
│-- 📄 relatorio_temperatura.xlsx  # Relatório em Excel
│-- 📊 boxplot_temperatura.png  # Gráfico de distribuição
│-- 📁 venv/  # Ambiente virtual
```

## 🛠 Solução de Problemas

Se ocorrerem erros:
- **Arquivo CSV não encontrado** → Verifique se o caminho está correto.
- **Erro ao importar bibliotecas** → Certifique-se de que está no ambiente virtual e instalou as dependências corretamente.
- **Problemas com venv no Windows** → Se o comando `activate` não funcionar, tente:
  ```bash
  Set-ExecutionPolicy Unrestricted -Scope Process
  .\venv\Scripts\activate
  ```

✅ **Agora você está pronto para rodar sua análise estatística!** 🚀

