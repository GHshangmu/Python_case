# 正则表达式库
import re
import requests
import xlwt

from bs4 import BeautifulSoup
start_url = 'https://tool.lu/school/index.html'


# 获得整页数据
def get_text(url):
    response = requests.get(url)
    # 设置编码格式
    response.encoding = 'utf-8'
    return response.text


# 使用字符串截取知识点获取所有高校数据
def get_item_by_str(text):
    item_list = []
    # 将整页数据拆为列表
    list_1 = text.split('<table width="100%" cellspacing="0" cellpadding="0" class="tbl">')
    # 将list_1的后半部分通过<tr>在拆一次
    list_2 = list_1[1].split('<tr>')[1:]
    for i in list_2:
        # 去除脏数据
        for tag in ['\n', ' ', '</td>', '<span style="color: #009A61;">', '</span>', '</tr>', '<tr>',
                    '<th width="40%">', '<th width="20%">', '</th>', '<span style="color: #E74C3C;">',
                    '</table>', '<p>注：<p>', '<spanstyle="color:#009A61;">', '<spanstyle="color:#E74C3C;">']:
            i = i.replace(tag, '')
        # 四个为一个列表进行组合
        little_item = i.split('<td>')[1:]
        # 将每个小列表添加到item_list中
        item_list.append(little_item)
    return item_list[1:]
# 使用正则表达式获取所有高校数据


def get_item_by_re(text):
    # 去除空格
    html = text.replace('\n', '').replace(' ', '')
    # 缩小范围
    rule_1 = re.compile(r'双一流</th></tr><tr>(.*)</table><p>注')
    table = rule_1.findall(html)
    # 正则取出数据
    rule_2 = re.compile('td>(.*?)</td><td><spanstyle="color:#[A-Za-z0-9]+;">(.*?)</span></td><td>'
                      '<spanstyle="color:#[A-Za-z0-9]+;">(.*?)</span></td><td>(.*?)</td></tr>')
    return rule_2.findall(table[0])


# 使用BeautifulSoup获取所有高校数据
def get_item_by_bs(text):
    # 创建BeautifulSoup实例
    bs = BeautifulSoup(text, 'html.parser')
    # 查找所有标签为tr的内容
    tag_tr = bs.find_all('tr')
    # 获取所有高校数据并转为数据表
    return [[i.get_text().strip() for i in tr.find_all('td')] for tr in tag_tr][1:-5]


# 设置单元格宽度
def set_width(sheet):
    # 设置第二列宽度
    col_2 = sheet.col(1)
    col_2.width = 256 * 20
    # 设置第五列宽度
    col_5 = sheet.col(4)
    col_5.width = 256 * 15

# 设置Excel样式
def set_sheet_style():
    # 创建第一行样式和全部样式实例
    all_style = xlwt.XFStyle()
    first_row_style = xlwt.XFStyle()
    # 设置边框线
    border = xlwt.Borders()
    border.top = xlwt.Borders.THIN
    border.bottom = xlwt.Borders.THIN
    border.left = xlwt.Borders.THIN
    border.right = xlwt.Borders.THIN
    # 使文字居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    # 设置字体为微软雅黑
    all_font = xlwt.Font()
    all_font.name = '微软雅黑'
    # 第一行设置为微软雅黑并字体加粗，字体大小为11
    first_row_font = xlwt.Font()
    first_row_font.name = '微软雅黑'
    first_row_font.bold = True
    first_row_font.height = 20 * 11
    # 将修改好的各个样式添加到样式实例中
    all_style.font = all_font
    all_style.alignment = alignment
    all_style.borders = border
    first_row_style.font = first_row_font
    first_row_style.alignment = alignment
    first_row_style.borders = border
    # 将样式返回
    return all_style, first_row_style


# 将数据写入表格
def write_item_in_sheet(sheet, item_list, style):
    # 获得行号列号
    for row in range(len(item_list)):
        # 生成表格编号
        sheet.write(row + 1, 0, row + 1, style)
        for col in range(len(item_list[row])):
            # 将高校信息数据写入到excel表格中
            sheet.write(row + 1, col + 1, item_list[row][col], style)


# 创建表格并指定标题
def save_in_excel(item_list):
    # 打开表格
    wbk = xlwt.Workbook()
    # 创建一个单元
    sheet = wbk.add_sheet('高校信息表V2.0')
    # 调用设置宽度方法设置单元格宽度
    set_width(sheet)
    # 调用设置样式方法，获得第一行样式和全部样式
    all_style, first_row_style = set_sheet_style()
    # 生成excel表格的标题
    title_list = ['编号', '学校名称', '985', '211', '双一流']
    # 将标题写入excel并设置样式
    for col in range(len(title_list)):
        sheet.write(0, col, title_list[col], first_row_style)
    # 将高校数据写入excel并设置样式
    write_item_in_sheet(sheet, item_list, all_style)
    # 保存excel表
    wbk.save('高校信息表V2.0.xls')


html = get_text(start_url)
item_list = get_item_by_re(html)
save_in_excel(item_list)
