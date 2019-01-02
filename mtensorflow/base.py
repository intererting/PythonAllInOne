import tensorflow as tf
import numpy as np


def testA():
    a = tf.constant(3.0, dtype=tf.float32)
    b = tf.constant(4.0, dtype=tf.float32)

    total = a + b

    sess = tf.Session()
    print(sess.run(total))
    print(sess.run((a, b, total)))
    print(sess.run({'a': a, "b": b, 'total': total}))


def testB():
    vec = tf.random_uniform(shape=(1, 3))
    sess = tf.Session()
    print(sess.run(vec))


def testC():
    x = tf.placeholder(tf.float32)


def testD():
    my_data = [
        [1, 2],
        [3, 4]
    ]

    slices = tf.data.Dataset.from_tensor_slices(my_data)
    nextItem = slices.make_one_shot_iterator().get_next()

    sess = tf.Session()
    while True:
        try:
            print(sess.run(nextItem))
        except tf.errors.OutOfRangeError:
            break


def testE():
    x = tf.placeholder(dtype=tf.float32, shape=[None, 3])
    linear_model = tf.layers.Dense(units=1)
    y = linear_model(x)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    print(sess.run(y, {x: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}))


if __name__ == '__main__':
    testE()
