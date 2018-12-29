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

# 限制窗体大小
root.maxsize(1040, 1025)
root.minsize(1040, 1025)


# 通过职业获取英雄
def get_hero_list_by_career(career):
    # 当点击按钮全部时，直接返回全部的英雄信息列表
    if career == 'all':
        return hero_info_list
    # 根据传入的职业名字筛选并新建英雄列表
    else:
        hero_list_select = []
        for i in hero_info_list:
            if i.get(career):
                hero_list_select.append(i)
        return hero_list_select


# 根据输入获取相应的角色列表
def get_hero_list_by_input(entry_text):
    # 重新布局frame，将查询出的图片从最左侧显示
    frame.grid(row=1, column=0, sticky=W)
    hero_list_select = []
    # 输入框有内容时，根据输入的内容进行模糊查询
    if entry_text:
        for i in hero_info_list:
            if i.get('name').find(entry_text) != -1:
                hero_list_select.append(i)
        return hero_list_select
    # 若输入框没有内容且确认按钮被点击，直接返回
    else:
        return


# 创建展示英雄部件
def widget_create(select_hero_list):
    # 删除原来的控件
    for widget in frame.winfo_children():
        widget.destroy()
    n = 0
    index_num = 0
    if select_hero_list:
        for i in select_hero_list:
            # 图片处理
            locals()['img' + str(i)] = Image.open(i.get('img_path'))
            locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
            # 创建Label标签，分别显示图片和文字
            locals()['label' + str(i)] = Label(frame, width=100, height=95, image=locals()['img' + str(i)])
            locals()['text' + str(i)] = Label(frame, text=i.get('name'))
            # 将创建好的Label标签进行布局
            locals()['label' + str(i)].grid(row=2 * (index_num // 10), column=n)  # 1 3 5 7 9 11 13
            locals()['text' + str(i)].grid(row=2 * (index_num // 10) + 1, column=n)  # 2 4 6 8 10 12
            index_num += 1
            n += 1
            if n == 10:
                n = 0
        root.mainloop()


# 主方法
def display_hero(btn_name):
    # 当按钮为确认按钮且输入框输入了内容，调用获取英雄列表和创建部件方法
    if btn_name == 'commit':
        if entry.get():
            hero_list = get_hero_list_by_input(entry.get())
            widget_create(hero_list)
    else:
        hero_list = get_hero_list_by_career(btn_name)
        widget_create(hero_list)


frame = Frame(root)
frame.grid(row=1, column=0, rowspan=8, columnspan=10)
# 创建不同职业的按钮
all = Button(root, text='全部', command=lambda: display_hero('all')).grid(row=0, column=0, padx=30, pady=10)
is_tank = Button(root, text='坦克', command=lambda: display_hero('is_tank')).grid(row=0, column=1, padx=30, pady=10)
is_warrior = Button(root, text='战士', command=lambda: display_hero('is_warrior')).grid(row=0, column=2, padx=30, pady=10)
is_assa = Button(root, text='刺客', command=lambda: display_hero('is_assa')).grid(row=0, column=3, padx=30, pady=10)
is_master = Button(root, text='法师', command=lambda: display_hero('is_master')).grid(row=0, column=4, padx=30, pady=10)
is_archer = Button(root, text='射手', command=lambda: display_hero('is_archer')).grid(row=0, column=5, padx=30, pady=10)
is_sup = Button(root, text='辅助', command=lambda: display_hero('is_sup')).grid(row=0, column=6, padx=30)
# 创建输入框
entry = Entry(root)
entry.grid(row=0, column=7, padx=20)
# 确认按钮
commit = Button(root, text='确定', command=lambda: display_hero('commit')).grid(row=0, column=8)

# 调用函数用于启动后就显示所有英雄信息
display_hero('all')

root.mainloop()
