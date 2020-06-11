import  urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import random

def proxy_user():
    url = "http://www.baidu.com/"


    proxy_list = [
        #可以将值中的http://省略
       {"http": "http://113.121.94.84:9999"},
       {"http": "http://175.42.158.133:9999"},
       {"http": "http://123.169.166.130:9999"},
       {"http": "http://49.70.17.226:9999"}
    ]

    for index,proxy in enumerate(proxy_list):
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            response = opener.open(url,timeout=4)
            str_response = response.read().decode("utf-8")
            file_name= "5.%d"%index + ".html"
            with open(file_name,"w",encoding="utf-8") as f:
                f.write(str_response)
        except Exception as e:
            print(e)
proxy_user()