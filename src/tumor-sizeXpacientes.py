# Pergunta 2: Qual o tamanho de tumor dos pacientes da idade com maior recorrência de câncer?


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
  
pd.set_option('display.max_rows', None)

# get dataframe from dataset csv
file_path = 'dataset/breast-cancer.csv'
dataframe = pd.read_csv(file_path)

# get new df with columns i will use
columns = ['recurrence', 'age', 'tumor-size']
df = dataframe[columns]

# sort df by age and tumor-size
df = df.sort_values(by=['age', 'tumor-size'])

# get df with recurrence-events
df = df[df['recurrence'] == 'recurrence-events']

# pega as idades mais frequentes
most_frequently_age = df['age'].mode()[0]
df = df[df['age'] == most_frequently_age]
print(df['age'].value_counts())

# ! Vou usar seaborn ao inves de matplotfodase

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(data=df, x='tumor-size', binwidth=5)
plt.title('Tamanho de tumor dos pacientes da idade com maior recorrência de câncer')
plt.xlabel('Tamanho do tumor')
plt.ylabel('COntagem de Pacientes')
plt.show()

