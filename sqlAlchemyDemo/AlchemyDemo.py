# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model.esModel import BizAugment
# 创建对象的基类:
Base = declarative_base()



# 初始化数据库连接:
engine = create_engine('mysql+pymysql://phoenix_es:phoenix_es@192.168.6.120:3306/phoenix_es')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


session = DBSession()
#增
# augMent = BizAugment()
# augMent.chapter_id = 100
# augMent.kp_id = 100
# session.add(augMent)
# session.commit()


# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
augMents = session.query(BizAugment).all() #.filter(BizAugment.id == '18')
# 打印类型和对象的name属性:
for augMent in augMents:
    print(augMent.kp_id)


session.close()