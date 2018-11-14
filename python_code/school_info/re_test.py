import re

test_str = '''
小王 手机号码：15478954564 邮箱：12356484557@sina.com 密码：qwer123 
小李 手机号码：18878456564 邮箱：dada_qqq@qq.com 密码：QQppp121 
小刘 手机号码：13022454564 邮箱：abc666@163.com 密码：1545454 
小吴 手机号码：15578958411 邮箱：545131ads@sda.com 密码：123645 
小郑 手机号码：15466475464 邮箱：assdasdfa@sina.com 密码：mingtian 
小赵 手机号码：13644887874 邮箱：1231eq143123@sina.com 密码：nihao
小孙 手机号码：13123444364 邮箱：1121112wqeq@ooo.com 密码：12qw12qw 
小郑 手机号码：18845456864 邮箱：dadad_dadad@sina.com 密码：qeqerqtad 
小张 手机号码：15478123131 邮箱：1234@126.com 密码：qQDA12wQEQ3
小冯 手机号码：15123144444 邮箱：qwe@sina.com 密码：WEQDAQ12121
'''

phone_rule = re.compile('(1[0-9]\d{9})')
mail_rule = re.compile('([0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[a-zA-Z]+)')
password_rule = re.compile('密码：([a-zA-Z0-9]+)')
result = phone_rule.findall(test_str)
print(result)
