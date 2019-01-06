import tensorflow as tf

a = tf.constant([[1, 2, 4], [3, 4, 5]])
b = tf.constant([[-1, 3], [4, 2], [5, 7]])

multiplicacao = tf.matmul(a, b)
print(multiplicacao)
type(multiplicacao)

with tf.Session() as sess:
    print(sess.run(multiplicacao))
