# 未设置cookies
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 可以看出未添加cookies时候，网页显示未登录
def cookies_use():
    url = "https://www.yaozh.com/member"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    str_response = response.read().decode("utf-8")
    with open("1.html","w",encoding="utf-8") as f:
        f.write(str_response)

cookies_use()