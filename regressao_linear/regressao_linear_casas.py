import numpy as np
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

y_modelo = b0 + b1 * xph
erro = tf.losses.mean_squared_error(yph, y_modelo)
otimizador = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
treinamento = otimizador.minimize(erro)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        indices = np.random.randint(len(x), size = batch_size)
        feed = {xph: x[indices], yph: y[indices]}
        sess.run(treinamento, feed_dict = feed)
        
    b0_final, b1_final = sess.run([b0, b1])
    
print(b0_final)
print(b1_final)
    
    
    
    
    
    
    

