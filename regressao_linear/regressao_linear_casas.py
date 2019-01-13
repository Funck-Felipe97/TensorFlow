import pandas as pd
base = pd.read_csv('C:/Users/funck/Desktop/Documentos/TensorFlow/regressao_linear/house_prices.csv')
base.head()
base.count()


# pegando a coluna com a metragem das casas
x = base.iloc[:, 5:6].values

# pegando todas as colunas com os preços das casas
y = base.iloc[:, 2:3]


# Escalonando valores
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
x = scaler_x.fit_transform(x)
scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)

import matplotlib.pyplot as plt
%matplotlib inline
plt.scatter(x, y)


import tensorflow as tf

b0 = tf.Variable(0.41)
b1 = tf.Variable(0.72)

batch_size = 32
xph = tf.placeholder(tf.float32, [batch_size, 1])
yph = tf.placeholder(tf.float32, [batch_size, 1])

