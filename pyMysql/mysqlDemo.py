import pymysql
from config.config import  dbconfig
from pymysql.cursors import Cursor,SSCursor

connection = pymysql.connect(**dbconfig)
cursor = Cursor(connection)

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = 'SELECT * from navbar where nav_id = 1'
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchone()
        print(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close();

