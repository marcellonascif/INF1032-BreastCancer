# Pergunta: Como os tamanhos de tumores influenciam na recorrência de eventos de câncer de mama?


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)

# get dataframe from dataset csv
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

columns = ['recurrence', 'tumor-size']
df = dataframe[columns]

print(df['tumor-size'].value_counts())

# sort df by age and tumor-size
df = df.sort_values(by=['tumor-size'])
# print(df)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='tumor-size', hue='recurrence', multiple='stack', binwidth=5)
plt.title('Tamanho do tumor em pacientes com e sem recorrência de eventos de Câncer de Mama')
plt.xlabel('Tamanho do tumor')
plt.ylabel('Contagem de Pacientes')
plt.show()