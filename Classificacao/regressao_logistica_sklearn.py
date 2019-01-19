import pandas as pd
base = pd.read_csv('C:/Users/funck/Desktop/Documentos/TensorFlow/Classificacao/census.csv')
base.head()

base.shape

x = base.iloc[:, 0:14].values
y = base.iloc[:, 14].values


# Trocando atributos categoricos por números
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder() 
x[:, 1] = label_encoder.fit_transform(x[:, 1])
x[:, 3] = label_encoder.fit_transform(x[:, 3])
x[:, 5] = label_encoder.fit_transform(x[:, 5])
x[:, 6] = label_encoder.fit_transform(x[:, 6])
x[:, 7] = label_encoder.fit_transform(x[:, 7])
x[:, 8] = label_encoder.fit_transform(x[:, 8])
x[:, 9] = label_encoder.fit_transform(x[:, 9])
x[:, 13] = label_encoder.fit_transform(x[:, 13])


#Normalizando os dados
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
x = scaler_x.fit_transform(x)

#Dividindo dados entre treinamento e testes
from sklearn.model_selection import train_test_split
x_treinamento, y_treinamento, x_teste, y_teste = train_test_split(x, y, test_size = 0.3)

#Criando classificador
from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression(max_iter = 10000)
classificador.fit(x_treinamento, y_treinamento)

previsoes = classificador.predict(x_teste)


from sklearn.metrics import accuracy_score
taxa_acerto = accuracy_score(y_teste, previsoes)








