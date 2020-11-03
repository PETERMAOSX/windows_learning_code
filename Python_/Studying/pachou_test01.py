from urllib import request
req = request.Request("http://fanyi.baidu.com/")
response = request.urlopen(req)
print("geturl 打印信息: %s"%(response.geturl()))
print('******************************************')
print("info 打印信息: %s"%(response.info()))
print('********************************************')
print("getcode 打印信息: %s"%(response.getcode()))
