from random import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

#创建连接对象也就是为了连接到本地的数据库
engine = create_engine('mysql+pymysql://root:root@localhost:3306/testdab',
                       encoding='utf-8',  # 编码格式
                       echo=True,  # 是否开启sql执行语句的日志输出
                       pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收（重置） （默认为-1）,其实session并不会被close
                       poolclass=NullPool  # 无限制连接数
                       )
		
#声名Base
Base = declarative_base()

# 创建会话
session = sessionmaker(engine)
mySession = session()

		
# 创建类，继承基类，用基本类型描述数据库结构
class User(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    Cgrade = Column(Integer, nullable=False)
    Mgrade = Column(Integer, nullable=False)
    Egrade = Column(Integer, nullable=False)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
	


# 插入100条数据
#for i in range(1,100):
#    user = User(id = i,name="小红",Cgrade = int(random()*100),Egrade = int(random()*100),Mgrade = int(random()*100))
#    mySession.add(user)
#mySession.commit()

#批量更改数据
#for i in range(1,100):
#    result = mySession.query(User).filter(User.id == i).first()
#    Cgrade = result.Cgrade + 5
#    sql = "update grade set Cgrade = %s where id = %s"
#    engine.execute(sql,(Cgrade,i))

for i in range(1,50):
    sql = "select name,Cgrade from grade where id = %s"
    result = engine.execute(sql,i)
    print(result.fetchall()) 

#根据id批量删除数据
#for i in range(1,100):
#    mySession.query(User).filter(User.id == i).delete()
#mySession.commit()


#sql语句查询
#result = engine.execute("select * from grade")
#print(result.fetchall()) 