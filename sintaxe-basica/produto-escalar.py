import tensorflow as tf

a = tf.constant([[-1.0, 7.0, 5.0]] ,name = 'entrada')
b = tf.constant([[0.8, 0.1, 0.0]], name = 'pesos')

multiplicacao = tf.multiply(a, b)    # Multiplicação entre os itens da matriz
soma = tf.reduce_sum(multiplicacao)  # Somando todos os itens da matriz multiplicação

with tf.Session() as sess:
    print(sess.run(a))
    print("\n")
    print(sess.run(b))
    print("\n")
    print(sess.run(multiplicacao))
    print("\n")
    print(sess.run(soma))