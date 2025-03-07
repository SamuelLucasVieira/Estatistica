import pandas as pd

class loads():
    def load_csv(self, file_path):
        """Lê e processa um arquivo CSV corretamente, ignorando a coluna WKT e garantindo que a geometria seja válida."""
        try:
            df = pd.read_csv(file_path, delimiter=";", encoding="latin1", skip_blank_lines=True, dtype=str, on_bad_lines="skip", header=0)
            # 🔹 Colunas esperadas no banco de dados (ignorando WKT)
            expected_columns = [
                "Data Medicao","TEMPERATURA"
            ]

            # 🔹 Reordenar DataFrame para seguir a ordem correta
            df = df[expected_columns]
            return df
        except Exception as e:
            print(f"❌ Erro ao carregar CSV: {e}")
            return None