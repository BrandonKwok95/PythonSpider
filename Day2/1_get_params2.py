import urllib.request
import urllib.parse
import string
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_params():
    url = "https://www.baidu.com/s?"

    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }
    # 下面方法将一个字典转化为字符串（名值对的形式）
    str_params = urllib.parse.urlencode(params)
    # 若带有中文应当再加入一次转换保证准确性
    final_params = urllib.parse.quote(str_params, safe=string.printable)
    final_url = url + final_params
    print(final_url)

    response = urllib.request.urlopen(final_url)
    str_response = response.read()

    # 二进制的解码（mac多数为utf-8;win多数为gbk）
    str_response = str_response.decode("utf-8")

    with open("1.html", "w", encoding="utf-8") as f:
        f.write(str_response)
get_params()