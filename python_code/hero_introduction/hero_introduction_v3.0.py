from tkinter import *
from PIL import Image
from PIL import ImageTk

hero_info_list = [
    {'index_num': 1, 'name': '米莱狄', 'img_path': ".\\hero_img\\米莱狄.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 2, 'name': '狂铁', 'img_path': ".\\hero_img\\狂铁.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 3, 'name': '弈星', 'img_path': ".\\hero_img\\弈星.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 4, 'name': '裴擒虎', 'img_path': ".\\hero_img\\裴擒虎.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 5, 'name': '杨玉环', 'img_path': ".\\hero_img\\杨玉环.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 6, 'name': '公孙离', 'img_path': ".\\hero_img\\公孙离.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 7, 'name': '明世隐', 'img_path': ".\\hero_img\\明世隐.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 8, 'name': '女娲', 'img_path': ".\\hero_img\\女娲.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 9, 'name': '梦奇', 'img_path': ".\\hero_img\\梦奇.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 10, 'name': '苏烈', 'img_path': ".\\hero_img\\苏烈.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 11, 'name': '百里玄策', 'img_path': ".\\hero_img\\百里玄策.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 12, 'name': '百里守约', 'img_path': ".\\hero_img\\百里守约.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 13, 'name': '铠', 'img_path': ".\\hero_img\\铠.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 14, 'name': '鬼谷子', 'img_path': ".\\hero_img\\鬼谷子.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 15, 'name': '干将莫邪', 'img_path': ".\\hero_img\\干将莫邪.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 16, 'name': '东皇太一', 'img_path': ".\\hero_img\\东皇太一.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 17, 'name': '大乔', 'img_path': ".\\hero_img\\大乔.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 18, 'name': '黄忠', 'img_path': ".\\hero_img\\黄忠.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 19, 'name': '诸葛亮', 'img_path': ".\\hero_img\\诸葛亮.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 20, 'name': '哪吒', 'img_path': ".\\hero_img\\哪吒.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 21, 'name': '太乙真人', 'img_path': ".\\hero_img\\太乙真人.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 22, 'name': '蔡文姬', 'img_path': ".\\hero_img\\蔡文姬.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 23, 'name': '雅典娜', 'img_path': ".\\hero_img\\雅典娜.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 24, 'name': '杨戬', 'img_path': ".\\hero_img\\杨戬.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 25, 'name': '成吉思汗', 'img_path': ".\\hero_img\\成吉思汗.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 26, 'name': '钟馗', 'img_path': ".\\hero_img\\钟馗.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 27, 'name': '虞姬', 'img_path': ".\\hero_img\\虞姬.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 28, 'name': '李元芳', 'img_path': ".\\hero_img\\李元芳.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 29, 'name': '张飞', 'img_path': ".\\hero_img\\张飞.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 30, 'name': '刘备', 'img_path': ".\\hero_img\\刘备.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 31, 'name': '后羿', 'img_path': ".\\hero_img\\后羿.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 32, 'name': '牛魔', 'img_path': ".\\hero_img\\牛魔.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 33, 'name': '孙悟空', 'img_path': ".\\hero_img\\孙悟空.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 34, 'name': '亚瑟', 'img_path': ".\\hero_img\\亚瑟.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 35, 'name': '橘右京', 'img_path': ".\\hero_img\\橘右京.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 36, 'name': '娜可露露', 'img_path': ".\\hero_img\\娜可露露.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 37, 'name': '不知火舞', 'img_path': ".\\hero_img\\不知火舞.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 38, 'name': '张良', 'img_path': ".\\hero_img\\张良.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 39, 'name': '花木兰', 'img_path': ".\\hero_img\\花木兰.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 40, 'name': '兰陵王', 'img_path': ".\\hero_img\\兰陵王.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 41, 'name': '王昭君', 'img_path': ".\\hero_img\\王昭君.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 42, 'name': '韩信', 'img_path': ".\\hero_img\\韩信.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 43, 'name': '刘邦', 'img_path': ".\\hero_img\\刘邦.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 44, 'name': '姜子牙', 'img_path': ".\\hero_img\\姜子牙.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 45, 'name': '露娜', 'img_path': ".\\hero_img\\露娜.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 46, 'name': '程咬金', 'img_path': ".\\hero_img\\程咬金.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 47, 'name': '安琪拉', 'img_path': ".\\hero_img\\安琪拉.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 48, 'name': '貂蝉', 'img_path': ".\\hero_img\\貂蝉.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 49, 'name': '关羽', 'img_path': ".\\hero_img\\关羽.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 50, 'name': '老夫子', 'img_path': ".\\hero_img\\老夫子.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 51, 'name': '武则天', 'img_path': ".\\hero_img\\武则天.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 52, 'name': '项羽', 'img_path': ".\\hero_img\\项羽.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 53, 'name': '达摩', 'img_path': ".\\hero_img\\达摩.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 54, 'name': '狄仁杰', 'img_path': ".\\hero_img\\狄仁杰.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 55, 'name': '马可波罗', 'img_path': ".\\hero_img\\马可波罗.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 56, 'name': '李白', 'img_path': ".\\hero_img\\李白.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 57, 'name': '宫本武藏', 'img_path': ".\\hero_img\\宫本武藏.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 58, 'name': '典韦', 'img_path': ".\\hero_img\\典韦.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 59, 'name': '曹操', 'img_path': ".\\hero_img\\曹操.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 60, 'name': '甄姬', 'img_path': ".\\hero_img\\甄姬.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 61, 'name': '夏侯惇', 'img_path': ".\\hero_img\\夏侯惇.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 62, 'name': '周瑜', 'img_path': ".\\hero_img\\周瑜.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 63, 'name': '吕布', 'img_path': ".\\hero_img\\吕布.jpg", 'is_tank': 1, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 64, 'name': '芈月', 'img_path': ".\\hero_img\\芈月.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 65, 'name': '白起', 'img_path': ".\\hero_img\\白起.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 66, 'name': '扁鹊', 'img_path': ".\\hero_img\\扁鹊.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 67, 'name': '孙膑', 'img_path': ".\\hero_img\\孙膑.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 68, 'name': '钟无艳', 'img_path': ".\\hero_img\\钟无艳.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 69, 'name': '阿轲', 'img_path': ".\\hero_img\\阿轲.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 70, 'name': '高渐离', 'img_path': ".\\hero_img\\高渐离.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 71, 'name': '刘禅', 'img_path': ".\\hero_img\\刘禅.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 72, 'name': '庄周', 'img_path': ".\\hero_img\\庄周.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 1},
    {'index_num': 73, 'name': '鲁班七号', 'img_path': ".\\hero_img\\鲁班七号.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 74, 'name': '孙尚香', 'img_path': ".\\hero_img\\孙尚香.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 1, 'is_sup': 0},
    {'index_num': 75, 'name': '嬴政', 'img_path': ".\\hero_img\\嬴政.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 76, 'name': '妲己', 'img_path': ".\\hero_img\\妲己.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 77, 'name': '墨子', 'img_path': ".\\hero_img\\墨子.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 78, 'name': '赵云', 'img_path': ".\\hero_img\\赵云.jpg", 'is_tank': 0, 'is_warrior': 1, 'is_assa': 1,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 79, 'name': '小乔', 'img_path': ".\\hero_img\\小乔.jpg", 'is_tank': 0, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 1, 'is_archer': 0, 'is_sup': 0},
    {'index_num': 80, 'name': '廉颇', 'img_path': ".\\hero_img\\廉颇.jpg", 'is_tank': 1, 'is_warrior': 0, 'is_assa': 0,
     'is_master': 0, 'is_archer': 0, 'is_sup': 0}
]

root = Tk()
root.title('英雄介绍')
root.maxsize(1180, 620)
root.minsize(1180, 620)


def display_heros(hero_career='all'):
    for widget in frame.winfo_children():
        widget.destroy()
    n = 0
    for i in hero_info_list:
        flag = False
        if hero_career == 'all':
            flag = True
        else:
            flag = i.get(hero_career)
        if flag:
            n += 1
            if n == 10:
                n = 0
            locals()['img' + str(i)] = Image.open(i.get('img_path'))
            locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
            locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
            locals()['text' + str(i)] = Label(frame, text=i.get('name'))
            index_num = i.get('index_num') - 1
            locals()['label' + str(i)].grid(row=index_num // 10 + 1, column=n)
            locals()['text' + str(i)].grid(row=index_num // 10 + 2, column=n)
    root.mainloop()


#
# def display_tank(hero_career):
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get(hero_career):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             n = index_list.index(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             else:
#                 locals()['label' + str(i)].grid(row=3, column=(index_list.index(i.get('index_num')) - 10))
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#     root.mainloop()
#
#
# def display_warrior():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get('is_warrior'):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             elif index_list.index(i.get('index_num')) < 20:
#                 locals()['label' + str(i)].grid(row=3, column=index_list.index(i.get('index_num')) - 10)
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#             else:
#                 locals()['label' + str(i)].grid(row=5, column=(index_list.index(i.get('index_num')) - 20))
#                 locals()['text' + str(i)].grid(row=6, column=index_list.index(i.get('index_num')) - 20)
#     root.mainloop()
#
#
# def display_assa():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get('is_assa'):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             else:
#                 locals()['label' + str(i)].grid(row=3, column=(index_list.index(i.get('index_num')) - 10))
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#     root.mainloop()
#
#
# def display_master():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get('is_master'):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             elif index_list.index(i.get('index_num')) < 20:
#                 locals()['label' + str(i)].grid(row=3, column=(index_list.index(i.get('index_num')) - 10))
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#             else:
#                 locals()['label' + str(i)].grid(row=5, column=(index_list.index(i.get('index_num')) - 20))
#                 locals()['text' + str(i)].grid(row=6, column=index_list.index(i.get('index_num')) - 20)
#     root.mainloop()
#
#
# def display_archer():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get('is_archer'):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             else:
#                 locals()['label' + str(i)].grid(row=3, column=(index_list.index(i.get('index_num')) - 10))
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#     root.mainloop()
#
#
# def display_sup():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     index_list = []
#     for i in hero_info_list:
#         if i.get('is_sup'):
#             locals()['img' + str(i)] = Image.open(i.get('img_path'))
#             locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
#             locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
#             locals()['text' + str(i)] = Label(frame, text=i.get('name'))
#             index_list.append(i.get('index_num'))
#             if index_list.index(i.get('index_num')) < 10:
#                 locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
#                 locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
#             else:
#                 locals()['label' + str(i)].grid(row=3, column=(index_list.index(i.get('index_num')) - 10))
#                 locals()['text' + str(i)].grid(row=4, column=index_list.index(i.get('index_num')) - 10)
#     root.mainloop()


# 查询英雄
def search_hero():
    for widget in frame.winfo_children():
        widget.destroy()
    index_list = []
    if entry.get():
        for i in hero_info_list:
            if i.get('name').find(entry.get()) != -1:
                print(i)
                locals()['img' + str(i)] = Image.open(i.get('img_path'))
                locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])

                locals()['label' + str(i)] = Label(frame, width=100, height=100, image=locals()['img' + str(i)])
                locals()['text' + str(i)] = Label(frame, text=i.get('name'))
                index_list.append(i.get('index_num'))
                print(index_list.index(i.get('index_num')))
                locals()['label' + str(i)].grid(row=1, column=index_list.index(i.get('index_num')))
                locals()['text' + str(i)].grid(row=2, column=index_list.index(i.get('index_num')))
                print()
        root.mainloop()


frame = Frame(root)
frame.grid(row=1, column=0, rowspan=8, columnspan=10)

button_names = ['全部', '坦克', '坦克', '坦克', '坦克', '坦克', '坦克']
func_list = [display_heros(), display_heros(), display_heros(), display_heros(), display_heros(), display_heros(),
             display_heros()]
for x in range(7):
    Button(root, text=button_names[x], command=func_list[x]).grid(row=0, column=(x + 1), padx=50)

entry = Entry(root)
entry.grid(row=0, column=8, padx=20)

btn8 = Button(root, text='确定', command=search_hero).grid(row=0, column=9)

root.mainloop()
