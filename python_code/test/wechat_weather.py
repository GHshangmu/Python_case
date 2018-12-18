import re
import json
import requests
import itchat
from itchat.content import *


def weather_info(uname, city):
    url = 'http://v.juhe.cn/weather/index?format=1&cityname=%s&key=9eedafbff727567b793ed3e72b83cd34' % city
    # 使用requests发起请求，接受返回的结果
    res = requests.get(url)
    # 使用loads函数，将json字符串转换为python的字典
    res_dict = json.loads(res.text)
    print(res_dict)
    # 取出error
    error_num = res_dict['error_code']
    # # 如果取出的error为0，表示数据正常，否则没有查询到结果
    if error_num == 0:
        # 从字典中取出所有天气数据
        results = res_dict['result']
        # 根据索引取出本日天气信息字典
        info_dict = results['today']
        # 根据字典的key，取出城市名称,日期，天气，风级，温度
        city_name = info_dict['city']
        date = info_dict['date_y']
        weather = info_dict['weather']
        wind = info_dict['wind']
        temperature = info_dict['temperature']
        advice = info_dict['dressing_advice']

        print('%s %s %s %s %s' % (city_name, date, weather, wind, temperature))
        print('本日建议：%s' % advice)
        itchat.send('%s %s %s %s %s' % (city_name, date, weather, wind, temperature), toUserName=uname)
        itchat.send('本日建议：%s' % advice, toUserName=uname)
    else:
        itchat.send("未找到该城市的天气哦，是不是输入错误了。", toUserName=uname)


# 如果对方发的是文字，则我们给对方回复以下的东西
@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('天气', msg['Text'])
    if match:
        city = msg['Text'][msg['Text'].find("+") + 1:]
        weather_info(msg['FromUserName'], city)


itchat.auto_login(enableCmdQR=True)
itchat.run()
