import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.array([[18], [23], [28], [33], [38], [43], [48], [53], [58] ,[63]])
y = np.array([[871], [1132], [1356], [1488], [1638], [1569], [1754], [1866], [1900], [2000]])


# Escalonando valores
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
x = scaler_x.fit_transform(x)
print(x)

scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)
print(y)


plt.scatter(x, y)

#realizando regressao com tensorflow

import tensorflow as tf

# coeficientes da regressao linear gerados com pesos aleatórios
b0 = tf.Variable(0.54)
b1 = tf.Variable(0.71)


# calculando erro para regressao linear
erro = tf.losses.mean_squared_error(y, (b0 + b1 * x)) 


# criando otimizador
otimizador = tf.train.GradientDescentOptimizer(learning_rate= 0.001)
treinamento = otimizador.minimize(erro)
init = tf.global_variables_initializer()

# realizando treinamento
with tf.Session() as sess:
    sess.run(init)
    
    #executar treinamento 100 vezes 
    for i in range(1000):
        sess.run(treinamento)
    b0_final, b1_final = sess.run([b0, b1])
    
print(b0_final)
print(b1_final)

#calculando previsoes para o x com o modelo treinado
previsoes = b0_final + b1_final * x

plt.plot(x, previsoes, color = 'red')
plt.plot(x, y, 'o')


# Nova previsao com transformações
previsao = scaler_y.inverse_transform(b0_final + b1_final * scaler_x.transform([[40]]))
print(previsao)


#calculado erros 

previsoes1 = scaler_y.inverse_transform(previsoes)
y1 = scaler_y.inverse_transform(y)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y1, previsoes1)
mse = mean_squared_error(y1, previsoes1)

print(mae)
print(mse)

































    