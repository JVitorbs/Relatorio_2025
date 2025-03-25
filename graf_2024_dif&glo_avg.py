import pandas as pd
import matplotlib.pyplot as plt

# Nome do arquivo de entrada
arquivo_entrada = "dados_filtrados_2024.dat"

# Lendo o arquivo, ignorando a primeira linha (cabeçalho inicial)
df = pd.read_csv(arquivo_entrada, skiprows=0)

# Removendo espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# Convertendo a coluna "TIMESTAMP" para datetime
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"], errors='coerce')

# Convertendo colunas de radiação para numérico e removendo negativos
df["glo_avg_2"] = pd.to_numeric(df["glo_avg_2"], errors="coerce")
df["dif_avg_2"] = pd.to_numeric(df["dif_avg_2"], errors="coerce")

# Filtrando apenas valores positivos
df = df[(df["glo_avg_2"] >= 0) & (df["dif_avg_2"] >= 0)]

# Criando o gráfico de dispersão
plt.figure(figsize=(10, 5))
plt.scatter(df["TIMESTAMP"], df["glo_avg_2"], color='b', label="Glo Avg 2", alpha=0.7)
plt.scatter(df["TIMESTAMP"], df["dif_avg_2"], color='r', label="Dif Avg 2", alpha=0.7)

# Configurações do gráfico
plt.xlabel("Tempo")
plt.ylabel("Irradiância (W/m²)")
plt.title("Dispersão de glo_avg_2 e dif_avg_2 ao longo do tempo")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()
