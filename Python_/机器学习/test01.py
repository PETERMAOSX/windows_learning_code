import tensorflow as tf
import numpy as np

x_date = np.random.rand(100).astype(np.float32)
y_date = x_date*0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([0]))

y = Weights*x_date + biases

loss = tf.reduce_mean(tf.square(y-y_date))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train= optimizer.minimize(loss)

init = tf.initialize_all_variables()


sess = ef.Sessioin()
sess.run(init) #Vary important

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(biases))
