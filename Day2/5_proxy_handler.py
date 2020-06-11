import  urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def create_proxy_handler():

    url = "https://www.baidu.com/"


    proxy = {
        #可以将值中的http://省略
        "http":"http://113.121.94.84:9999"
    }

    proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建opener
    opener = urllib.request.build_opener(proxy_handler)
    repsonse = opener.open(url).read()
    str_response =  repsonse.decode("utf-8")
    print(str_response)

    with open("5.html","w",encoding="utf-8") as f:
        f.write(str_response)

create_proxy_handler()