import tensorflow as tf

x = [[1, 1, 2], [2, 3, 1]]
print tf.reduce_sum(x, reduction_indices=[1])