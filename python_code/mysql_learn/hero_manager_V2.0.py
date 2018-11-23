import pymysql


def excute_sql(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "mysql_learn")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
        db.close()


def insert_hero():
    r_name = input('请输入英雄名')
    r_skill = input('请输入英雄技能')
    r_hp = int(input('请输入英雄血量'))
    r_birthplace = input('请输入英雄出生地')
    # SQL 插入语句
    sql = """INSERT INTO role(r_name,
    r_skill, r_hp, birth_place)
    VALUES ('%s', '%s', '%d', '%s')"""%(r_name, r_skill, r_hp, r_birthplace)
    excute_sql(sql)


def delete_hero():
    input_type = input("输入all删除全部英雄，输入one删除单个英雄")
    if input_type == 'all':
        # SQL 删除语句
        sql = '''DELETE FROM role'''
        excute_sql(sql)
    if input_type == 'one':
        name = input('请输入你要删除的英雄名')
        # SQL 删除语句
        sql = """DELETE FROM role WHERE r_name = '%s'""" % (name)
        excute_sql(sql)


def update_hero():
    input_type = input('你想要修改什么?')
    input_value = input('请输入修改后的值')
    r_name = input('请输入你要修改的英雄')
    # SQL 更新语句
    sql = """UPDATE role SET %s= '%s' WHERE r_name = '%s'""" % (input_type, input_value, r_name)
    excute_sql(sql)




def select_hero():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "mysql_learn")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = """SELECT * FROM role"""
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print('职业名', '职业技能', '职业血量', '职业出生地')
    for row in results:
        r_name = row[0]
        r_skill = row[1]
        r_hp = row[2]
        birth_place = row[3]
        print(r_name, r_skill, r_hp, birth_place)


def main():
    print("欢迎来到英雄管理系统:输入1新增英雄,输入2进行英雄的删除,输入3进行英雄的修改,输入4进行英雄的查询")
    num = int(input('请输入'))
    if num == 1:
        insert_hero()
    elif num == 2:
        delete_hero()
    elif num == 3:
        update_hero()
    elif num == 4:
        select_hero()
    else:
        print('请按提示输入...')


if __name__ == '__main__':
    while True:
        main()
