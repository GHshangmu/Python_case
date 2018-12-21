import base64
import urllib

from aip import AipFace

APP_ID = '11725560'
API_KEY = 'KzW4iAYa8CdSkSVXnlFnH6CP'
SECRET_KEY = 'Q1RkG3tGirdfukxmC5V6AfwcgVazXZGy'
# 创建网络请求的客户端
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
# image = "http://5b0988e595225.cdn.sohucs.com/images/20180429/3d664a25f7ef4f4fa27236582b8ebfb8.jpeg"
# image = "http://s9.rr.itc.cn/r/wapChange/20172_18_3/a43ngq2608044945661.jpeg"
# imageType = "URL"

imageType = "BASE64"
list = []

f = open(r"C:\Users\m_sha\Desktop\胡歌.jpg", 'rb')
data = base64.b64encode(f.read())
image = str(data, "UTF-8")

# 指定服务器都返回哪些数据
options = {"face_field": "age,beauty,gender"}
result = client.detect(image, imageType, options)
print(result)
face_data = result.get("result").get("face_list")[0]
print("年龄：%s" % face_data.get("age"))
print("颜值：%s" % face_data.get("beauty"))
print("性别：%s" % face_data.get("gender").get("type"))
