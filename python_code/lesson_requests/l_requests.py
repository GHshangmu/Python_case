import requests
import json
# res = requests.get('http://www.httpbin.org')
# # print(res.text)
#
#
# res = requests.get('http://www.httpbin.org/get', params={'username': 'cloudream'})
# print(res.url)
# print(res.text)
import requests
from PIL import Image
from io import BytesIO
# 二进制数据
# res = requests.get('http://pic29.nipic.com/20130511/9252150_174018365301_2.jpg')
# img = Image.open(BytesIO(res.content))
# img.save(r"C:\Users\m_sha\Desktop\test.jpg")

# res = requests.get('http://httpbin.org/get')
# print(res.json())

form = {'username': 'cloud', 'password': '123456'}
res = requests.post('http://httpbin.org/post', data=form)
print(res.headers)
# res = requests.post('http://httpbin.org/post', data=json.dumps(form))
# print(res.text)



headers = {
    'User‐Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87Safari/537.36'
}
res = requests.post('http://www.ucai.cn/index.php?app=fullstack&mod=Public&act=doLogin',
                    data={
                        'account': 'chen@ucai',
                        'password': '111111',
                        'remember': 'undefined'}, headers=None)
print(res.text)

