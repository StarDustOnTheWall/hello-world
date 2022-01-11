import tensorflow as tf

v_1 = tf.constant([[1, 2], [3, 4]])
v_1.numpy()
line = tf.linspace(1.0, 10.0, 4, name="linspace")
number_range = tf.range(start=1, limit=10, delta=2)
a = tf.constant([1., 2., 3., 4., 5., 6.], shape=[2, 3])
b = tf.constant([7., 8., 9., 10., 11., 12.], shape=[3, 2])
c = tf.linalg.matmul(a, b)  # 矩阵乘法
w = tf.Variable([1.0])  # 新建张量
with tf.GradientTape() as tape:  # 追踪梯度
    loss = w * w
grad = tape.gradient(loss, w)  # 计算梯度

model = tf.keras.Sequential()