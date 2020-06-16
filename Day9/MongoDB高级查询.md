# 高级查询

- `db.collectionName.findOne({})`找出符合条件的一个文档
- `db.collectionName.find({}).pretty()`使输出格式更加美观

## 比较运算符
- 小于 less than`$lt`
- 小于等于 less than equal`$lte`
- 等于
- 大于等于 greater than equal  `$gte`
- 大于 greater than`$gt`
- 不等于 not equal `$ne`

`db.collectionName.find({age:{$gte:18}})` 找出大于等于18的文档

## 范围运算符
- 在范围内（特定值） `{$in:[]}`
- 不在范围内 `{$nin:[]}`
- 与上相同 `{$not:{$in:[]}}`

`db.superstar.find({age:{$in:[28,40]}}).pretty()` 找出28和40年龄范围内的文档


## 逻辑运算符
- 与 `{$and:[]}`
- 或 `{$or:[]}`
- 非 `{$not:[]}`

`db.superstar.find({$or:[{age:28},{team:'Lakers'}]}).pretty()` 找出年龄为28或者队伍为Lakers的文档

## 正则表达式
- `{key:/value/}`查找符合相关条件的文档
- `{key:{$regex:""}}`

`db.superstar.find({name:{$regex:"James"}})`
`db.superstar.find({name:/James/})`找到名字包含James的文档

## 自定义查询
- `db.superstar.find({$find:where:function(){return this.age>30;}})` 利用JS语言便携


## limit,skip,count,distinct
- `db.superstar.find().limit()` 限制查询文档数

- `db.superstar.find().skip()` 跳过开头文档数

- `db.superstar.find({}).count()` 查询文档数

- `db.superstar.count({})` 与上相同

- `db.superstar.distinct(age,{})` 查询不重复的数据，返回列表


## 投影（即特定取数据）
默认情况下，_id是显示的
`db.superstar.find({},{name:0,age:0}).pretty()` 0表示不显示，1表示显示（不可混用），最好只用

## 排序
`db.superstar.find().sort({age:-1})` -1为降序，1为升序
