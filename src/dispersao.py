import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

# Função para converter a faixa etária em um valor numérico (ponto médio)
def convert_age_to_midpoint(age_range):
    age_split = age_range.split('-')
    if len(age_split) == 2:
        return (int(age_split[0]) + int(age_split[1])) / 2
    return int(age_split[0])

# Aplicar a função na coluna de idade
dataframe['age_midpoint'] = dataframe['age'].apply(convert_age_to_midpoint)

# Selecionar colunas relevantes
columns = ['age_midpoint', 'deg-malig', 'recurrence']
df = dataframe[columns]

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age_midpoint', y='deg-malig', hue='recurrence', palette='Set1')
plt.title('Relação entre Idade, Grau de Malignidade e Recorrência de Câncer de Mama')
plt.xlabel('Idade (ponto médio da faixa etária)')
plt.ylabel('Grau de Malignidade')
plt.legend(title='Recorrência')
plt.tight_layout()

# Mostrar o gráfico
plt.show()
