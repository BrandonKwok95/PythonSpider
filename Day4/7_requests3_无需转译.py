# Requests可以不用转译
import requests
# 参数自动转译
url = "https://www.baidu.com/s?"
params = {
    "wd":"白癜风撒风"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
response = requests.get(url, headers=headers, params=params)
str_response = response.content.decode("utf-8")

with open("7.html","w",encoding="utf-8") as f:
    f.write(str_response)

# 发送post请求和添加参数也是类似

#requests.post(url,data)