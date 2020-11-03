import paddle
import paddle.nn.functional as F
import numpy as np

paddle.disable_static()
print(paddle.__version__)

a = paddle.randn([4, 2])
b = paddle.arange(1, 3, dtype='float32')

print(a.numpy())
print(b.numpy())

c = a + b
print(c.numpy())

d = paddle.matmul(a, b)
print(d.numpy())
