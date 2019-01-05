numero = 2

vetor = [2,3,5]

import numpy as np
vetor = np.asarray(vetor)

vetor.max()
vetor.argmax()
vetor.min()
vetor.mean()
vetor.sum()

vetor2 = numero * vetor; # Multiplicando numero por vetor

np.arange(1, 50, 3)    # criando vetor
np.zeros(10)           # criando vetor com valores zerados
np.zeros((3,3))        # criando matriz
np.ones(10)            # criando vetor com valores 1  

np.linspace(1, 20, 10) # cria um vetor de 10 posições com o numero 1 inicial e 0 20 final

np.random.randint(0, 101)
np.random.randint(0, 101, 3)      # gera um vetor aleatório
np.random.randint(0, 101, (3,3))  # gera uma matriz aleatória

vetor3 = np.linspace(1, 10, 10)
matriz = vetor3.reshape(2, 5)     # modifica a estrutur de dados

matriz[0,2]                      # pega o valor da linha 0 e coluna 2
matriz[:, 2]                     # pega o elemento da coluna 2 de todas as linhas
matriz[:, 0:2]


x = np.arange(1,11)
y = x**2

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x, y, 'x',color = 'red')




