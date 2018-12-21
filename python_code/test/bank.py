
key = 9527

# for i in range(3):
#     password = int(input('请输入密码'))
#     if password == key:
#         while True:
#             money = int(input('请输入金额'))
#             if money % 100 == 0 and money <= 1000:
#                 print('您取了%s元'%money)
#                 print('请取卡')
#                 break
#             else:
#                 print('金额输入有误，请重新输入')
#     if i == 2:
#         print('密码输入错误')

chance = 0
while True:
    password = int(input('请输入密码'))
    if password == key:
        while True:
            money = int(input('请输入金额'))
            if money % 100 == 0 and money <= 1000:
                print('您取了%s元' % money)
                print('请取卡')
                break
            else:
                print('金额输入有误，请重新输入')
    if chance == 2:
        print('密码输入错误')
        break
    chance += 1

[1,2].reverse()

