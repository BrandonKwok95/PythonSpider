import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def load_data():
    url = "https://www.baidu.com/"
    #get请求（http请求）


    response = urllib.request.urlopen(url)
    print(response)

    #读取内容
    data = response.read()
    print(data)
    str_data = data.decode("utf-8")
    print(str_data)

    with open("first_baidu.html","w",encoding="utf-8") as f:
        f.write(str_data)
        #可以用decode和encode对爬取数据进行数据转换decode("utf-8") 或者encode("utf-8")
load_data()