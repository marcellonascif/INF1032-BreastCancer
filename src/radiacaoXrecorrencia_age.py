import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
file_path = 'dataset/breast-cancer.csv'  # Substitua com o caminho correto do seu arquivo
cancer_data = pd.read_csv(file_path)

# Configuração do estilo visual para os gráficos
sns.set(style="whitegrid")

# Gráfico 2: Distribuição de Casos por Grau de Malignidade e Recorrência
plt.figure(figsize=(10, 6))
sns.countplot(x='deg-malig', hue='recurrence', data=cancer_data, palette="muted")
plt.title('Distribuição de Casos de Câncer de Mama por Grau de Malignidade e Recorrência')
plt.xlabel('Grau de Malignidade')
plt.ylabel('Número de Casos')
plt.legend(title='Recorrência', loc='upper right')
plt.tight_layout()
plt.show()
