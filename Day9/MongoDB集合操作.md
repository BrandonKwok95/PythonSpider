# 聚合指令（aggregate指令）

## 常用表达式

- `$sum:value` 计算总和(value代表统计的倍数)
`db.superstar.aggregate({$group:{_id:"$age",count:{$sum:1}}})`
- `$avg` 计算均值
`db.superstar.aggregate({$group:{_id:"$age",count:{$sum:2},avg:{$avg:"$age"}}})`
- `$min` 获取最小值
- `$max` 获取最大值
- `$push` 在结果文档中插入一个数组
- `$first` 获取第一个元素
- `$last` 获取最后一个元素

## aggregate基本语句（可以将一个结果交付给下一个结果）
- $group{_id:"key"}将集合中的文档分组，利于统计结果

```
//根据age分组
db.superstar.aggregate({$group:{_id:"$age"}})
//将获取整个集合数据，并根据文档个数计算sum
db.superstar.aggregate({$group:{_id:"$null",count:{$sum:1}}})
//将获取整个集合数据，并根据文档个数计算sum，最后算出平均年龄
db.superstar.aggregate({$group:{_id:"$null",count:{$sum:1},age_avg:{$avg:"$age"}}})
//db.superstar.aggregate($group:{_id:{"name":"$name","age":"$age","team":"$team"}}) 可以把重复值去除

```
- $project修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档

```
//将age的值赋给_id,然后将_id隐藏起来
//无需某个字段可以直接置零
db.superstar.aggregate({$group:{_id:"$age",count:{$sum:2},avg:{$avg:"$age"}}},{$project:{age:"_id",count:"$count",avg:"$avg",_id:0}})


```

-$match可以筛选数据
```
//筛选出大于30的数据
db.superstar.aggregate({$match:{age:{$gt:30}}}).pretty()
//筛选出年龄大于等于数据29的数据，根据队伍进行分组，后改_id名为team
db.superstar.aggregate({$match:{age:{$gte:29}}},{$group:{_id:"$team"}},{$project:{team:"$_id",_id:0}})
```
