#机器学习第一步，数据预处理
import numpy as np #导入库
import matplotlib.pyplot as plt
x,y = [],[] #构建数组来储存值，数据集
for sample in open("H:\prices.txt","r"): #读取数据 sample 对应的正是一个个样本
    _x,_y = sample.split(",") #由于数据是用逗号隔开的，所以使用python中的split方法隔开
    x.append(float(_x)) #将字符串数据转化为浮点数
    y.append(float(_y))

#读取完数据后，将数据转化为npmpy数组方便进一步的处理
x,y = np.array(x),np.array(y)
#标准化 使用公式 x = (x-x.mean())/x.std()
x = (x-x.mean())/x.std()
#将原始数据以散点图的形式画出来
plt.figure()
plt.scatter(x,y,c='g',s=6) #两个维度数据的关联程度
#plt.show()

x0 = np.linspace(-2,4,100) #在(-2,4)这个区间上面取100个点作为画图的基础

#利用numpy的函数定义训练并且返回多项式回归模型的函数
#deg参数代表着模型参数中的n，即是模型中多项式的次数
#返回的模型能够根据输入的x(默认是x0)，返回相对应的预测的y

def get_model(deg):
    return lambda input_x=x0:np.polyval(np.polyfit(x,y,deg),input_x)

#根据参数n，输入的x,y返回相对应的损失

def get_cost(deg,input_x,input_y):
    return 0.5*((get_model(deg)(input_x)-input_y)**2).sum()
#定义测试参数集并且根据它进行各种实验

test_set = (1,4,10)
for d in test_set:
    #输出相应的损失
    print(get_cost(d,x,y))

#画出相应的图像
plt.scatter(x,y,c='g',s=20)
for d in test_set:
    plt.plot(x0,get_model(d)(),label="degree={}".format(d))

#将x轴的范围和y轴的范围限制在(-2,4),(10^5,8x10^5)
plt.xlim(-2,4)
plt.ylim(1e5,8e5)
#调用legend()方法使曲线相对应的label正确显示
plt.legend()
plt.show()