import tensorflow as tf

valor1 = tf.constant(15, name = 'valor1')
print(valor1)

var = tf.Variable(valor1 + 5, name = 'valor1')
print(var)

init = tf.global_variables_initializer()  # Necessario para inicializar as variaveis

with tf.Session() as sess:
    sess.run(init)
    s = sess.run(var)
    
print(s)