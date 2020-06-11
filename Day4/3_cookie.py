"""
手动设置cookie过于繁琐
因此，可以使用代码登陆后，获取响应的报文中的cookie

基本步骤
    1.代码登陆
    2。代码带着cookie去访问个人中心

"""
import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#cookiejar可以自动保存cookie
from http import cookiejar

def auto_cookie():
    # 1.代码登陆
    # 1.1登陆地址
    # 1.2登陆信息
    login_form_data = {
        #可以在页面找到相应的formash和backurl的值
        "username": "15871688074",
        "pwd": "xin665968",
        "formhash": "4A95C39D38",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    # data参数需要转码（字典到字符串），并设置为二进制形式
    # 因为post请求中的data需要的是二进制类型
    str_form_data = urllib.parse.urlencode(login_form_data).encode("utf-8")
    # 1.3发送登陆请求
    cookie_jar = cookiejar.CookieJar()
    # 有添加cookie的处理器
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(cookie_handler)
    # 添加请求头并发送请求
    login_url = "https://www.yaozh.com/login/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    login_request = urllib.request.Request(login_url, headers=headers, data=str_form_data)
    # 登陆请求后，opener会自动保存相应的cookie
    login_response = opener.open(login_request)


    # 2.利用cookiejar可以获取cookie，进而再去发送请求
    url = "https://www.yaozh.com/member"
    request = urllib.request.Request(url, headers=headers)
    response = opener.open(request)
    str_response = response.read().decode("utf-8")
    with open("3.html", "w", encoding="utf-8") as f:
        f.write(str_response)

auto_cookie()

