import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
file_path = 'dataset/breast-cancer.csv'  # Substitua com o caminho correto do seu arquivo
cancer_data = pd.read_csv(file_path)

# Configuração do estilo visual para os gráficos
sns.set(style="whitegrid")

# Preparação dos dados para o Gráfico 2
grouped_data = cancer_data.groupby(['deg-malig', 'recurrence']).size().unstack()
proportion_data = grouped_data.div(grouped_data.sum(axis=1), axis=0)

# Gráfico 2: Proporção de Recorrência por Grau de Malignidade
plt.figure(figsize=(10, 6))
proportion_data.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e'], ax=plt.gca())
plt.title('Proporção de Recorrência por Grau de Malignidade')
plt.xlabel('Grau de Malignidade')
plt.ylabel('Proporção de Casos')
plt.legend(title='Recorrência', loc='upper left')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
