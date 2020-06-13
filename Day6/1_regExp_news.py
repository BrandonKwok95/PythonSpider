import re
import requests

url = "http://news.baidu.com/"

response = requests.get(url)
str_response = response.content.decode("utf-8")
with open("1.html","w",encoding="utf-8") as f:
    f.write(str_response)

# 就可以爬取到所有a标签
pattern = re.compile('<a (.*?)/a>')
result = pattern.findall(str_response)
print(len(result))