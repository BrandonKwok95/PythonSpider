import requests
import json
url = "https://api.github.com/user"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
response = requests.get(url,headers=headers)
# 从二进制转为字符串
data = response.content.decode("utf-8")
# 此时json字符串实际含义是一个字典，但我们不利于索引出其相应值
print(data)
# 故利用json来实现(即可实现响应值的获取)将json字符串转化为字典
data = json.loads(data)
print(data["message"])

# 第二种方法(直接利用json读取)
print("\n********直接利用response.json()获取内容************\n")
data = response.json()
print(data)
print(data['message'])