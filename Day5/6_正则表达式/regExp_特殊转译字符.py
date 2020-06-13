import re
# .可以匹配换行符以外的任意字符
str = "我是红色\n我是绿色\n我是蓝色\n我是黄色\n"
# complie是形成正则表达式
pattern = re.compile(r'.色')     # r表示原始字符串，防止转义
# findall找出所有的文本，返回一个数组
result = pattern.findall(str)
print(result)


# *表示匹配前面的子表达式任意次（包括零次）,常与点共同使用（.*匹配任意字符任意次数，常用作某个字符后面紧跟着的所有字符）
# *会一直进行直到换行
str = "我是，红色\n我是，绿色\n我是，蓝色\n我是，黄色\n，"
pattern = re.compile(r'，.*')
result = pattern.findall(str)
print(result)

# +表示前面的子表达式表示一次或多次（不包括零次）
str = "我是，红色\n我是，绿色\n我是，蓝色\n我是，黄色色\n，"
pattern = re.compile(r'色.+')
result = pattern.findall(str)
print(result)

#? 表示零次或者一次

# {}表示匹配次数(可以指定具体次数，也可以指定上下限)
str = "啊啊啊啊，啊啊啊啊啊啊，啊啊啊啊啊啊啊啊，啊啊"
pattern = re.compile(r'啊{5,}')
result = pattern.findall(str)
print(result)

# .*+都是贪婪模式（尽可能多的匹配）
str = "<html><head><top><large><dad>"
pattern = re.compile(r'<.*>')
result = pattern.findall(str)
# ['<html><head><top><large><dad>']把整个字符串打印下来，不是我们想要的效果
print(result)
# 因此要引入非贪婪模式("尽可能的少")
pattern = re.compile(r'<.*?>')
result = pattern.findall(str)
print(result)

# 转义还有其他的特殊字符再次省略
str="橙子.绿色橙子.蓝色\n橙子.红色\n"
pattern = re.compile('.*\.')
result = pattern.findall(str)
print(result)

# []表示数字范围
#[a-c]表示a到c的字符 和 [msi]表示查找字符串中m或s或i
#方括号中特殊字符失效[.]就是表示.这个字符
#[^a]表示非a的字符
str="666688886"
pattern = re.compile('[0-6]{2,4}')
result = pattern.findall(str)
print(result)

# ^在单行模式下表示整个文本的开头
#  在多行模式下表示文本每行的的开头位置
str="001-苹果-5\n002-雪梨-6\n001-哈密瓜-7\n"
pattern = re.compile('\d+')
result = pattern.findall(str)
# ['001', '5', '002', '5', '001', '5']
print(result)

pattern = re.compile('^\d+')
result = pattern.findall(str)
# ['001'] 此时^表示整个文本的开头（单行模式）
print(result)

# re.M表示开启多行模式
pattern = re.compile('^\d+',re.M) #re.M或者re.MULTILINE相同
result = pattern.findall(str)
# ['001'] 此时^表示每行的开头（多行模式）
print(result)

# $在单行模式下表示整个文本的结尾
#  在多行模式下表示文本每行的的结尾位置
pattern = re.compile('\d+$',re.M) #re.M或者re.MULTILINE相同
result = pattern.findall(str)
# ['001'] 此时^表示每行的开头（多行模式）
print(result)

# ()表示组选择
# 可以通过某种特征定位，而且不提取出该特征
# 可以同时利用两个组提取，返回元祖
str = "我是，红色\n我是，绿色\n我是，蓝色\n我是，黄色色\n，"
pattern = re.compile('，(.+)',re.M)
result = pattern.findall(str)
# ['001'] 此时^表示每行的开头（多行模式）
print(result)

