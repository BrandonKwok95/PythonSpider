# 本节体现第三方库Requests相应的信息获取

import requests
class SpiderRequest(object):
    def __init__(self):
        url = "https://www.baidu.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content

        # 获取请求头
        request_headers  = self.response.request.headers
        print(request_headers)
        # 获取响应头
        response_headers = self.response.headers
        print(response_headers)
        # 获取响应吗
        response_code = self.response.status_code
        print(response_code)
        # 获取请求cookie
        # 取值为空，因为cookie可能是浏览器自动添加的，所以不会
        request_cookie = self.response.request._cookies
        print(request_cookie)
        # 获取响应cookie
        response_cookie = self.response.cookies
        print(response_cookie)
SpiderRequest().run()