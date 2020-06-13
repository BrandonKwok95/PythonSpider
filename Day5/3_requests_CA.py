import requests
url = "https://www.baidu.com"
# 取消ssl验证
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
response = requests.get(url=url, headers=headers,verify=False)
data = response.content.decode("utf-8")
print(data)
with open("3.html","w",encoding="utf-8") as f:
    f.write(data)