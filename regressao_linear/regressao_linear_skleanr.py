import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.array([[18], [23], [28], [33], [38], [43], [48], [53], [58] ,[63]])
print(x)

y = np.array([[871], [1132], [1356], [1488], [1638], [1569], [1754], [1866], [1900], [2000]])
print(y)


plt.scatter(x, y)


from sklearn.linear_model import LinearRegression

regression = LinearRegression();
regression.fit(x, y)               # Treinando modelo

# Coeficioente Y
regression.intercept_

#Coeficiente de x
regression.coef_

#criando previsão
previsao = regression.predict([[40]])
print(previsao)

previsao2 = regression.predict(x)
print(previsao2)


#calculando erro
resultado = abs(y - previsao2)
print(resultado)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y, previsao2)
mse = mean_squared_error(y, previsao2)
print(mae)
print(mse)


plt.plot(x, y, 'x')
plt.plot(x, previsao2, color = 'red')
plt.title("Regressao linear simples")
plt.xlabel("idade")
plt.ylabel("Custo")



