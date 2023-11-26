# Pergunta 3: Qual a distribuição de época de menopausa dos pacientes com e sem recorrência de eventos de câncer de mama?


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)

# get dataframe from dataset csv
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

columns = ['recurrence', 'menopause']
df = dataframe[columns]

# print(df['menopause'].value_counts())

# sort df by age and tumor-size
df = df.sort_values(by=['menopause'])
print(df)

sns.set(style="whitegrid")
# plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='menopause', hue='recurrence', multiple='stack', binwidth=5)
plt.title('Distribuição de Idades em Pacientes com e sem Recorrência de Eventos de Câncer de Mama')
plt.xlabel('Idade Média')
plt.ylabel('Contagem de Pacientes')
plt.show()