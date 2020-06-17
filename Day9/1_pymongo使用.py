from pymongo import MongoClient
class TestMongo(object):
    def __init__(self):
        # 选择端口号
        client  = MongoClient(host="127.0.0.1",port=27017)
        # 选择数据库和集合
        self.collection = client['python']['pythonmongo']

    def test_insert(self):
        ret = self.collection.insert({"name":"test_python","age":"ToT"})
        print(ret)

    def test_insert_multi(self):
        ret = self.collection.insert({"name":"test_mongo2"+str(i),'age':123} for i in range(10))

        '''
        item_list = [{"name":"test{}".format(i)} for i in range(10)]
        print(item_list)
        ret = self.collection.insert_many(item_list)
        '''
    def find_one(self):
        # 不可以连续查询同一个对象，相当于遍历一次后，游标对象到最后位置（类似与不可以连续对文件进行read语句，可以利用list(t)来解决）
        t = self.collection.find_one({"name":"test9"})
        print(t)

    def update_one(self):
        self.collection.update_one({"name":"test9"},{"$set":{"name":"kwok"}})
        self.collection.update_many({"age": 123}, {"$set": {"model": "RNN"}})

    def delete(self):
        self.collection.delete_many({"model":"RNN"})
        self.collection.delete_one({"name":"test7"})
    def run(self):
        pass

TestMongo().delete()