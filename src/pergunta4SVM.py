# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Carregando o conjunto de dados
file_path = 'dataset/breast-cancer.csv'
df = pd.read_csv(file_path)

y = df['recurrence']  # Classes
X = df.drop(columns=['recurrence'])  # Dados dos pacientes

age_avg = {
    '20-29': 24.5,
    '30-39': 34.5,
    '40-49': 44.5,
    '50-59': 54.5,
    '60-69': 64.5,
    '70-79': 74.5
    }

menopause_num = {
    'premeno': 0,
    'lt40'   : 1,
    'ge40'   : 2
    }

tumor_size_avg = {
    '0-4'  : 2,
    '5-9'  : 7,
    '10-14': 12,
    '15-19': 17,
    '20-24': 22,
    '25-29': 27,
    '30-34': 32,
    '35-39': 36.5,
    '40-44': 42,
    '45-49': 47.5,
    '50-54': 52
    }

inv_nodes_avg = {
    '0-2'  : 1,
    '3-5'  : 4,
    '6-8'  : 7,
    '9-11' : 10,
    '12-14': 13,
    '15-17': 16,
    '18-20': 19,
    '21-23': 22,
    '24-26': 25
    }

node_caps_num = {
    'no': 0,
    'yes' : 1
    }

breast_num = {
    'left' : 0,
    'right': 1
    }

breast_quad_num = {
    'left_up'   : 0,
    'left_low'  : 1,
    'right_up'  : 2,
    'right_low' : 3,
    'central'   : 4
    }

irradiat_num = {
    'no' : 0,
    'yes': 1
    }

# print(y)

X['age'] = X['age'].map(age_avg)
X['menopause'] = X['menopause'].map(menopause_num)
X['tumor-size'] = X['tumor-size'].map(tumor_size_avg)
X['inv-nodes'] = X['inv-nodes'].map(inv_nodes_avg)
X['node-caps'] = X['node-caps'].map(node_caps_num)
X['breast'] = X['breast'].map(breast_num)
X['breast-quad'] = X['breast-quad'].map(breast_quad_num)
X['irradiat'] = X['irradiat'].map(irradiat_num)


# Dividindo os dados em conjuntos de treinamento e teste #0.40 é teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Criando um classificador SVM
svm_classifier = svm.SVC(C=0.5, kernel='linear', gamma='auto')

# Treinando o modelo usando os conjuntos de treinamento
svm_classifier.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = svm_classifier.predict(X_test)
# print(y_pred)

# Avaliando o desempenho do modelo
# accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Imprimindo os resultados
# print(f"Acurácia: {accuracy}")
# print("\nMatriz de Confusão:")
# print(confusion_mat)
print("\nRelatório de Classificação:")
print(classification_rep)

# Matriz de confusão
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Visualizando a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['No Recurrence', 'Recurrence'], yticklabels=['No Recurrence', 'Recurrence'])
plt.title('Matriz de Confusão para o Classificador SVM')
plt.ylabel('Verdadeiro')
plt.xlabel('Previsto')
plt.show()

print("\nRelatório de Classificação:")
print(classification_rep)
