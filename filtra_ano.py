import pandas as pd

# Nome do arquivo original e do arquivo filtrado
arquivo_entrada = "RN-NAT-Natal-CR1000X_NAT_TD.dat"
arquivo_saida = "dados_filtrados_2024.dat"

# Lendo o arquivo, ignorando a primeira linha (cabeçalho inicial)
df = pd.read_csv(arquivo_entrada, skiprows=1)

# Filtrando apenas o ano de 2024
df_filtrado = df[df["Year"] == 2024]

# Salvando o arquivo filtrado sem alterar o formato original
df_filtrado.to_csv(arquivo_saida, index=False, quoting=1)  # quoting=1 mantém as aspas

print(f"Arquivo filtrado salvo como {arquivo_saida}")
