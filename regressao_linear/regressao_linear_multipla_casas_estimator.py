import pandas as pd
base = pd.read_csv('C:/Users/funck/Desktop/Documentos/TensorFlow/regressao_linear/house_prices.csv')
base.head()

#pegando as colunas da base de dados
base.columns

colunas_usadas = ['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']


base = pd.read_csv(
            'C:/Users/funck/Desktop/Documentos/TensorFlow/regressao_linear/house_prices.csv',
             usecols = colunas_usadas
        )


#Escalonando os dados com o método MinMax
from sklearn.preprocessing import MinMaxScaler
scaler_x = MinMaxScaler();
base[['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']] = scaler_x.fit_transform(base[['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']])

base.head()


scaler_y = MinMaxScaler();
base[['price']] = scaler_y.fit_transform(base[['price']])


x = base.drop('price', axis = 1)
y = base.price


# Criando os numerics columns
previsores_colunas = colunas_usadas[1:17]
previsores_colunas

import tensorflow as tf
colunas = [tf.feature_column.numeric_column(key = c) for c in previsores_colunas]


# dividindo os dados para treinamento
from sklearn.model_selection import train_test_split
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, test_size = 0.3)

x_treinamento.shape
y_treinamento.shape


# Criando funções de treinamento e teste
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x = x_treinamento, y = y_treinamento,
                                                         batch_size= 32, num_epochs = None, shuffle = True)

funcao_teste = tf.estimator.inputs.pandas_input_fn(x = x_teste, y = y_teste,
                                                         batch_size= 32, num_epochs = 10000, shuffle = False)

# criando metricas de treinamento
regressor = tf.estimator.LinearRegressor(feature_columns=colunas)

regressor.train(input_fn = funcao_treinamento, steps = 10000)

metricas_treinamento = regressor.evaluate(input_fn = funcao_treinamento, steps= 10000)


#criando metricas de previsão
funcao_previsao = tf.estimator.inputs.pandas_input_fn(x = x_teste, shuffle=False)
previsoes = regressor.predict(input_fn=funcao_previsao)

valores_previsoes = []
for p in regressor.predict(input_fn=funcao_previsao):
    valores_previsoes.append(p['predictions'])
    
valores_previsoes
    
import numpy as np    
valores_previsoes = np.asarray(valores_previsoes).reshape(-1,1)
valores_previsoes = scaler_y.inverse_transform(valores_previsoes)
valores_previsoes 

# Transformando y_teste em matriz
y_teste2 = y_teste.values.reshape(-1,1)

y_teste2 = scaler_y.inverse_transform(y_teste2)

y_teste2

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_teste2, valores_previsoes)
mae  
    
    
























