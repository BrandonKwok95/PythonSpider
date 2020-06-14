import requests
from bs4 import BeautifulSoup
import json

class Spider_bs4(object):
    def __init__(self):
        self.base_url = "https://bbs.hupu.com/yingchao-"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

        self.cookies = "cookie: _dacevid3=51be3b4f.4332.b96c.1636.3ef0399a1dff; _cnzz_CV30020080=buzi_cookie%7C51be3b4f.4332.b96c.1636.3ef0399a1dff%7C-1; __gads=ID=deff7b3d6877a83e:T=1591862128:S=ALNI_MarqJz5mzfU1NiqquZddPd1A3ZL-w; PHPSESSID=3600300153fef90590b0a1a009de3683; amvid=3587825342c6a4200676d798bd270b6b; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1592143238,1592143242,1592143247,1592143261; _HUPUSSOID=7c113525-06d4-4fdd-8e1d-b5a6759f2963; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a260712031a-082b49677fa767-143f6257-1296000-172a2607121b32%22%2C%22%24device_id%22%3A%22172a260712031a-082b49677fa767-143f6257-1296000-172a2607121b32%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=76b20f7115921457681303002e572f9bb616bf18e866852523ab146dd83a0d; _CLT=b0c2a05996d8b48b354e1fa4ddfc1fef; u=27171908|5pm66IO95LqR5aSH6IOO|2ea4|8a09b9c368d27bd9cbac78640252c061|68d27bd9cbac7864|aHVwdV9jYWE4NWY4NGZjNGE5YzRj; us=725a88a0fcc2b751658459b42664bb9eba35cdcf639017b929d765c8e366ab2535178d40a26c3724b21e27bb995bcee93ac3d00bb1d78e205a327ff9db207aa8; ua=176905092; _fmdata=osXeQBGeFnt4%2FSuoTSaSo0Go3KyrZ2TCStxdkjUWNqOqjcvpI6gsKPN0Ioegb%2BUYTKXnBeJ23xcNX1acXhsJy0gAcptKnZlORiBGuU%2Bj0Bg%3D; __dacevst=53e2add3.bb58217a|1592147713023; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1592145914"
        self.cookies_list = self.cookies.split("; ")
        self.cookies_dict = {}
        for cook in self.cookies_list:
            self.cookies_dict[cook.split("=")[0]] = cook.split("=")[1]

    def get_response(self,url):
        response = requests.get(url,headers=self.headers,cookies= self.cookies_dict)
        str_response = response.content.decode("utf-8")
        return str_response

    def parse_response(self,response):
        soup = BeautifulSoup(response,'lxml')
        # 获取对象：标题，作者，最后回复日期，链接
        result_title = soup.select('.truetit')
        result_author = soup.find_all(attrs={"class": "author box"})
        news_list = []
        url = "https://bbs.hupu.com"
        for index,title in enumerate(result_title):
            news_dict = {}
            news_dict["title"] = result_title[index].get_text()
            news_dict["url"] = url + result_title[index].get('href')
            news_dict["author&publish"] = result_author[index].get_text()
            news_list.append(news_dict)
        return news_list

    def save_response(self,data):
        str_list = json.dumps(data)
        with open('4.json','w',encoding="utf-8") as f:
            f.write(str_list)

    def run(self):
        total_list = []
        for page in range(1, 16):
            # 拼接完整url
            url = self.base_url + str(page)
            print(url)
            # 发送请求
            page_data = self.get_response(url)
            news_list = self.parse_response(page_data)
            total_list += news_list
        self.save_response(total_list)


Spider_bs4().run()