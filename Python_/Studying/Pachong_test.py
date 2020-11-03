from urllib import request
f = request.urlopen('http://fanyi.baidu.com')
data = f.read()
print('StatusL',f.status,f.reason,)
for k,v in f.getheaders():
    print('%s: %s ' %(k,v))