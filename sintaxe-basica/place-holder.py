import tensorflow as tf

p = tf.placeholder('float', None)   # O segundo parametro indica o tamanho do placeholder

operacao = p + 2
print(operacao)
type(operacao)

with tf.Session() as sess:
    resultado = sess.run(operacao, feed_dict = {p: [1, 3 , 5]})
    print(resultado)
    
p2 = tf.placeholder('float', [None, 5])  # placeholder com N linhas e 5 colunas
operacao2 = p2 * 5

with tf.Session() as sess:
    dados = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    resultado = sess.run(operacao2, feed_dict = {p2: dados})
    print(resultado)