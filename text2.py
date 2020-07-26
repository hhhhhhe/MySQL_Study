#import
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
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64),nullable=False)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
	
#sql语句查询
result = engine.execute("select * from students")
print(result.fetchall()) 

# 查询第一条
#result = mySession.query(User).first()
#print(result.name) #打印对象属性

# 查询所有
#result = mySession.query(User).all()
#print(result[0])

# 查询id为2的
#result = mySession.query(User).filter_by(id=2).first()
#print(result.name)

# 分页查询 0,2
#result = mySession.query(User).filter(User.id>1).limit(2).offset(0).all()
#print(result)

#插入新数据
#user = User(name="小红")
#mySession.add(user)
#mySession.commit()
#result = mySession.query(User).filter_by(name="小红").first()
#print(result.name)


#修改已有数据
#mySession.query(User).filter(User.name=="小红").update({"name":"小白"})
#mySession.commit()
#result = mySession.query(User).filter_by(name="小白").first()
#print(result.name)

#删除数据
#mySession.query(User).filter(User.id == 1).delete()
#mySession.commit()
#result = mySession.query(User).first()
#print(result.name) #打印对象属性
