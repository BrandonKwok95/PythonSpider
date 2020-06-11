import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def load_data():
    url = "https://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "HAHA": "hehe"
    }
    # 创造请求对象
    request = urllib.request.Request(url, headers=headers)
    # 还可以利用add_headerd来添加信息
    # request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")

    # 可以利用请求报文来作为url
    response = urllib.request.urlopen(request)
    str_response = response.read().decode("utf-8")

    # 请求头信息
    request_headers = request.headers
    print(request_headers['User-agent'])
    # 还可以调用get_header()来获取header内容(注意首字母大写)
    print(request.get_header("Haha"))

    print(str_response)
    # 利用该方法获取url连接
    # print(request.get_full_url())

    with open("2.html","w",encoding="utf-8") as f:
        f.write(str_response)


load_data()