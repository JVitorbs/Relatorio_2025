import pandas as pd
import matplotlib.pyplot as plt

# Nome do arquivo de entrada
arquivo_entrada = "dados_filtrados_2024.dat"

# Lendo o arquivo, ignorando a primeira linha (cabeçalho inicial)
df = pd.read_csv(arquivo_entrada, skiprows=0)

# Convertendo a coluna "TIMESTAMP" para datetime
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"], errors='coerce')

# Removendo valores NaN da coluna "glo_avg_2"
df = df.dropna(subset=["glo_avg_2"])

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(df["TIMESTAMP"], df["glo_avg_2"], marker='o', linestyle='-', color='b', label="glo_avg_2")

# Configurações do gráfico
plt.xlabel("Tempo")
plt.ylabel("Irradiância Global (W/m²)")
plt.title("Variação de glo_avg_2 ao longo do tempo")
plt.xticks(rotation=45)  # Rotaciona datas para melhor visualização
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()
