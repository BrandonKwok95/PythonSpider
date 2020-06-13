import re
# 将字符串中的数字乘以10
string = "A2134VDF231"
def multiple(matched):
    s = matched.group()
    s = int(s) * 10
    s = str(s)
    return s
# 正则表达式会给replace_string(第二个参数)传餐
result = re.sub("\d",multiple,string)

print(result)