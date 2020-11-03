import paddle
# 动态图模式
paddle.disable_static()
# 训练集
train_dataset = paddle.vision.datasets.MNIST(mode='train',chw_format=False)
# 测试集
val_dataset = paddle.vision.datasets.MNIST(mode='test',chw_format=False)
# 通过Sequential将一层一层的网络结构组建起来。
# 通过数据集加载接口的chw_format参数我们已经将[1, 28, 28]形状的图片数据改变形状为[1, 784]，那么在组网过程中不在需要先进行Flatten操作。
mnist = paddle.nn.Sequential(
    paddle.nn.Linear(784, 512),
    paddle.nn.ReLU(),
    paddle.nn.Dropout(0.2),
    paddle.nn.Linear(512, 10)
)

model = paddle.Model(mnist)
model.prepare(
    paddle.optimizer.Adam(parameters=mnist.parameters()),
    paddle.nn.CrossEntropyLoss(),
    paddle.metric.Accuracy()
)
model.fit(train_dataset,epochs=5,batch_size=32,verbose=1)
model.evaluate(val_dataset, verbose=0)