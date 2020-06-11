import requests

url = "https://www.baidu.com"
# get报文
response = requests.get(url)
print(response)

# 响应报文共有三个种类
# 优先使用content（text可能出错）
print("text数据\n%s" % response.text)
print("content数据\n%s" % response.content)
print("json数据\n%s" % response.json())