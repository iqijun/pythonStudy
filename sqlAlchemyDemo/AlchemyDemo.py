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
augMent = BizAugment()
augMent.chapter_id = 100
augMent.kp_id = 100

session = DBSession()
session.add(augMent)
session.commit()
session.close()