# 数据的备份和恢复
## 数据的备份
`mongodump -h dbhost -d dbname -o dbdirectory`
- `-h`  服务器地址，也可以是端口号(本机备份可忽略)
- `-d`  备份数据库名称
- `-o`  备份数据位置

## 数据的恢复
`mongodump -h dbhost -d dbname --dir dbdirectory`
- `-h`  服务器地址，也可以是端口号
- `-d`  备份数据库名称
- `--dir`  备份数据位置
