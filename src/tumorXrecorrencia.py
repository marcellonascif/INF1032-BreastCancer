import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

# Selecionar as colunas relevantes
columns = ['tumor-size']
df = dataframe[columns]

# Contagem de casos por tamanho de tumor
tumor_size_counts = df['tumor-size'].value_counts()

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
tumor_size_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c(range(len(tumor_size_counts))))
plt.title('Proporção de Tamanhos de Tumor em Todos os Casos de Câncer de Mama')
plt.ylabel('')  # Removendo o label do eixo y para melhorar a estética
plt.show()
