# MongoDB 数据库指令
## 创建数据库
- `use databaseName`    直接创建数据库
- `show databases`      查看所有数据库
- `db.dropDatabase()`   删除相应数据库
- `db`                  查看当前数据库

## 集合指令
对于不存在集合，首次假如数据，集合就会被创建出来
- `db.createCollection(name,options)` 手动创建集合
- `db.createCollection("status",{capped:true,size:10})`其中capped表示上限，size表示上限大小（假如超过指定值，将会覆盖之前的数据）
- `show collectionName`查看集合
- `db.collectionName.drop()`删除集合

## 数据类型
- Object ID 文档ID(12字节的十六位进制数：i.前4字节位当前时间戳) ii.接下来3字节位机器ID iii.接下来2字节服务进程id iv.最后3字节简单的增量值）
- String
- Boolean
- int
- double 浮点数
- Arrays
- Object json中的字典
- Null
- Timestamp 时间戳
- Date 日期（格式为new Date('1995-11-16')）

## 文档指令(增删查改)
- `db.collectionName.insert()`插入文档，若id值相同，将插入失败
- `db.collectionName.save()`插入文档，若id值相同，将更新文档
- `db.collectionName.find()`查看集合中的所有文档
- `db.collectionName.update({},{})`*直接替换*
- `db.collectionName.update({},{$set:{}},{multi:true})`*更新多条*
- `db.collectionName.remove({},{justOne:rue})`删除单条文档（justOne默认参数为false）
