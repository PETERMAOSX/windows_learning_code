import numpy as np
# arr = np.arange(10)
# brr = arr[arr % 2 == 1] #若要在数据中做判断的话，就在数组后面加上[类似于判断]
# print(brr)
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# c = np.concatenate([a,b],axis=0)
# print(c)
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# c = np.concatenate([a,b],axis=1)
# print(c)
# a = np.array([1,2,3])
# b = np.r_[np.repeat(a,2),np.tile(a,3)] #这是干嘛啊? 难道是np.repeat(每一个制重复3次)tile(全体重复3次)
# print(b) #Nice

# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# c = np.intersect1d(a,b)  #获取两个数组的交集
# print(c)
# a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# c = np.setdiff1d(a,b)  #删除交集
# print(c)

#np.where() 是获取数值位置的

a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5)&(a<=10))
b = a[index]
print(b)
