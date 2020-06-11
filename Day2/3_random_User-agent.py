#利用多代理来躲避服务器限制

import urllib.request
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def load_baidu():

    url = "https://www.baidu.com/"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ]

    #每次请求浏览器不同
    random_user_agent = random.choice(user_agent_list)

    request = urllib.request.Request(url)
    request.add_header("User-Agent",random_user_agent)

    response = urllib.request.urlopen(request)
    str_response = response.read().decode("utf-8")
    print(str_response)


    print(request.get_header("User-agent"))

load_baidu()