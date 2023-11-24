# Pergunta 1: Qual a distribuição de idades em pacientes com e sem recorrência de eventos de câncer de mama?


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)

# get dataframe from dataset csv
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

columns = ['recurrence', 'age']
df = dataframe[columns]

print(df['age'].value_counts())

# sort df by age and tumor-size
df = df.sort_values(by=['age'])
# print(df)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', hue='recurrence', multiple='stack', binwidth=5)
plt.title('Distribuição de Idades em Pacientes com e sem Recorrência de Eventos de Câncer de Mama')
plt.xlabel('Idade Média')
plt.ylabel('Contagem de Pacientes')
plt.show()