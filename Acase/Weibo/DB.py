import pymongo
from enum import Enum


# 定义存储类型枚举
class DbType(Enum):
    MONGO = 'mongo'
    MYSQL = 'mysql'
    REDIS = 'redis'




class DB:

    def save(self, type, data):
        print('使用%s来存储数据'%type)
        if type == DbType.MONGO:
            mongo_db = MongoDB()
            mongo_db.insert(data)
            pass




class MongoDB:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017
        # self.user_name = 'test'
        # self.user_pwd = '123456'
        self.db_name = 'weibo'
        self.collection_name = 'mongo'

    def insert(self, data):
        mongo_py = None
        try:
            # 1.链接mongod的服务
            mongo_py = pymongo.MongoClient("%s:%d" % (self.host, self.port))
            #mongo_py[self.db_name].authenticate(self.user_name, self.user_pwd)

            # 2.库和表的名字; 有数据会自动建库建表
            db = mongo_py[self.db_name]

            # 表 集合
            collection = db[self.collection_name]

            collection.insert_many(data)

            # 3.插入数据
            # one = {"name": "张三", "age": 50}
            # two_many = [
            #     {"name": "小三", "age": 50},
            #     {"name": "李四", "age": 30},
            #     {"name": "王五", "age": 20},
            #     {"name": "小刘", "age": 15}
            # ]

            # collection.insert_one(one)
            # collection.insert_many(two_many)
            # collection.insert()

        except Exception as e:
            print(e)
        finally:
            # 关闭数据库
            if mongo_py is not None:
                mongo_py.close()


