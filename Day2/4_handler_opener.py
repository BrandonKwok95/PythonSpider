import  urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def handler_opener():
    # 解决了urlopen无法自定义IP地址
    # SSL安全套接层 ssl第三方的CA数字证书
    # http端口号80 https443
    # urlopen为什么可以处理数据 handler处理器（方式）

    url = "https://www.baidu.com/"

    # 创建一个新的handler的处理器
    handler = urllib.request.HTTPHandler()
    # 自己创建一个opener来调用open方法调用请求数据
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)

    print(response)

    data = response.read().decode("utf-8")
    print(data)
    with open("4.html","w",encoding="utf-8") as f:
        f.write(data)


handler_opener()