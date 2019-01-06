import tensorflow as tf

vetor = tf.constant([1,2,3,4], name = 'vetor')
type(vetor)
print(vetor)

soma = tf.Variable(vetor + 4, name = 'soma')
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(soma))
    

valor = tf.Variable(0, name = 'valor')
init2 = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init2)
    for i in range(5):
        valor = valor + 1
        print(sess.run(valor))

