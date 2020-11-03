from aip import AipSpeech

APP_ID = '16431143'
API_KEY = 'ItTERW5SlKfoxtZavSiKZNDi'
SECRET_KEY = 'vtyENiidpxWwjAuuibssdo0LsG3AIyon'
#init login
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

text = client.asr(get_file_content('test.wav'), 'wav', 16000, {'lan': 'zh',})
print(text)
