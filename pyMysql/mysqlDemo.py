import pymysql
from config.config import  dbconfig
from pymysql.cursors import Cursor,SSCursor,DictCursor

connection = pymysql.connect(**dbconfig)


# 执行sql语句
# try:
#     with DictCursor(connection) as cursor:
#         # 执行sql语句，进行查询
#         sql = 'SELECT nav_id,nav_text from navbar where nav_id = 1'
#         cursor.execute(sql)
#         # 获取查询结果
#         result = cursor.fetchone()
#         print(result)
#     # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
#     connection.commit()
#
# finally:
#     connection.close();

try:
    with DictCursor(connection) as cursor:
        # 执行sql语句，进行查询
        sql = 'INSERT INTO navbar (nav_text,nav_url,nav_order)VALUES(%(text)s,%(url)s,%(order)s)'
        cursor.execute(sql,{"text":"python","url":"/python","order":"10"})
        # 获取查询结果
        # result = cursor.fetchone()
        # print(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close();
