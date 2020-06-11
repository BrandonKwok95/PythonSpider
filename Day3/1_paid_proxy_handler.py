import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def paid_proxy_use():
    #直接利用字典创建
    money_proxy = {"http":"username:pwd@192.168.1.1:80"}
    proxy_handler = urllib.request.ProxyHandler(money_proxy)
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open("http://www.baidu.com")
    print(response.read())

    '''
    #第二种方法(推荐，速度快)
    #第一步
    username = "abcname"
    pwd="123456"
    proxy_money = "123.124.23.233:8888"

    #第二步 创建密码管理器
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    #参数1：uri定位；参数2：url资源定位符；参数3：user；参数4：pwd
    password_manager.add_password(None, proxy_money, username, pwd)

    #第三步 创建可以验证的代理ip的代理器
    handler_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)

    #第四步 创建处理器opener
    opener_auth = urllib.request.build_opener(handler_auth_proxy)

    #第五步 发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())
    '''



paid_proxy_use()