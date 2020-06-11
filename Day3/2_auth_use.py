import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 访问自己的数据

def auth_innernet():
    # 第一步 用户名和密码
    user = "admin"
    pwd = "admin123"
    inner_url = "http://192.168.179.66"

    # 第二步 创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None,inner_url,user,pwd)

    # 第三步 创造认证处理器
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    # 第四步 创建处理器
    auth_opener = urllib.request.build_opener(auth_handler)

    # 第五步 发送请求
    response = auth_opener.open(inner_url)

    print(response.read())

auth_innernet()