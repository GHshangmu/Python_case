import pymysql


def welcome():
    print('欢迎进入英雄管理系统')
    print('请登录...')
    u_name = input('请输入用户名')
    u_password = input('请输入密码')
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "mysql_learn")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM USER_INFO WHERE u_name = '%s' AND u_password = '%s'" % (u_name, u_password)

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    if results:
        print('登陆成功')
    else:
        print('账号或密码错误')
    db.close()


def register():
    u_name = input('请输入用户名')
    u_password = input('请输入密码')
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "mysql_learn")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO USER_INFO
    (u_name, u_password) 
    VALUES (%s,%s)""" % (u_name, u_password)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        # 关闭数据库连接
        db.close()


def role_list():
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

    get_num = input('你想要查什么？')
    # 如果按1，查询血量大于100的职业
    if get_num == '1':
        sql = """SELECT * FROM role where r_hp > '%d'""" % (100)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)

        # 如果按下2，使用内连接查询相同地点的角色表中的角色姓名、血量和boss表中的boss名
    if get_num == '2':
        sql = """
            SELECT
            t1.r_name,
            t1.r_hp,
            t2.b_name
            FROM
            role t1
            INNER JOIN boss t2 ON t1.birth_place = t2.birth_place;
"""
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)

    if get_num == '3':
        sql = """
            SELECT
            t1.r_name,
            t1.r_hp,
            t2.b_name
            FROM
            role t1
            INNER JOIN boss t2 ON t1.birth_place = t2.birth_place;
    """
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)

    if get_num == '4':
        sql = """
            SELECT
            t1.r_name,
            t1.r_hp,
            t2.b_name
            FROM
            role t1
            LEFT JOIN boss t2 ON t1.birth_place = t2.birth_place;
    """
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results4 = cursor.fetchall()
        print(results4)

    if get_num == '5':
        sql = """
            SELECT
            t1.r_name,
            t1.r_hp,
            t2.b_name
            FROM
            role t1
            RIGHT JOIN boss t2 ON t1.birth_place = t2.birth_place;
    """
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results5 = cursor.fetchall()
        print(results5)

    if get_num == '6':
        sql = """
            SELECT
                    *
            FROM
                    role
            WHERE
                r_hp > (
                        SELECT
                                r_hp
                        FROM
                                role
                        WHERE
                        r_name = '赛利亚'
                        );
    """
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results6 = cursor.fetchall()
        print(results6)

    if get_num == '7':
        r_name = input('输入英雄名')
        r_skill = input('输入英雄技能')
        r_hp = input('输入英雄血量')
        birth_place = input('输入英雄出生地')
        sql = """
            INSERT INTO role(r_name, r_skill, r_hp, birth_place) VALUE ('%s', '%s', '%d', '%s' )
    """ % (r_name, r_skill, int(r_hp), birth_place)
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()



if __name__ == '__main__':
    role_list()
