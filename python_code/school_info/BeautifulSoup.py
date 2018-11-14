from bs4 import BeautifulSoup

html = '''...'''

bs = BeautifulSoup(html, 'lxml')

# 简单的获取数据的方法：
print('文档的title:', bs.title)
print('title的name属性:', bs.title.name)
print('title的内容:', bs.title.string)
print('title的parent名称,也就是上一级名称:', bs.title.parent.name)  # 获取
print('文档中第一个p节点:', bs.p)  # 获取
print('文档中第一个p节点的内容:', bs.p.get_text())  # 获取
print('第一个p节点的class内容:', bs.p['class'])  # 获取
print('文档的第一个a节点:', bs.a)  # 获取
print('文档中所有的a节点,返回一个list:', bs.find_all('a'))  # 获取
print('文档中id属性为a2的节点:', bs.find(id='a2'))  # 获取
