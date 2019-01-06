import tensorflow as tf

a = tf.constant([9,8,7], name = 'a')
b = tf.constant([1,2,3], name = 'b')

soma = a + b
type(soma)
print(soma)

with tf.Session() as sess:
    print(sess.run(soma))
    

a1 = tf.constant([[1, 2, 3], [4, 5, 6]], name = 'a1')
a2 = tf.constant([[1, 2, 3], [4, 5, 6]], name = 'a2')

soma1 = tf.add(a1, a2)
type(soma1)
print(soma1)

with tf.Session() as sess:
    print(sess.run(soma1))
    
    

a3 = tf.constant([[1, 2, 3], [4, 5, 6]])
a4 = tf.constant([[1], [4]])

soma2 = tf.add(a3, a4)

with tf.Session() as sess:
    print(sess.run(soma2))