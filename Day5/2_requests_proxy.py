# 使用代理
import requests

url = "https://www.baidu.com"
proxy_list = {"http": "https://58.61.154.153:8080"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
response = requests.get(url=url,proxies=proxy_list, headers=headers)
print(response.status_code)