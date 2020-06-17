## 索引
- 利用JS语句`for(i=0;i<10000;i++){db.t255.insert({name:"test"+i,age:i})}`创建10000个对象
- `db.t255.ensureIndex({name:1})`; 与上相比速度更快1和-1影响排序情况，其他应用不太重要
- 解释情况：不添加索引时，利用`_id`查找；添加索引可使查找速度更快

- 查看当前集合的所有索引 `db.collectionName.getIndexes()`
- 删除索引`db.collectionName.dropIndex('索引名称')`
