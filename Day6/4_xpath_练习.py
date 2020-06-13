
import requests
from lxml import etree
import json
# https://www.8btc.com/weekly?page=2
class Spider(object):
    def __init__(self):

        self.base_url = "https://www.8btc.com/weekly?page="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }
    # 发送请求
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        str_response = response.content.decode("utf-8")
        return str_response
    # 解析数据
    def xpath_reponse(self,response):
        xpath_data = etree.HTML(response)
        # 爬取出来网址
        result_href = xpath_data.xpath('//div[@class="bbt-col-xs-8"]/a/@href')
        # 爬取新闻标题
        result_title = xpath_data.xpath('//div[@class="weekly-item__title"]//text()')
        result_tag = xpath_data.xpath('//div[@class="weekly-item__tag"]/text()')
        url_href = "https://www.8btc.com"
        print(result_title)
        result_href = [url_href+href for href in result_href]
        news_list = []
        print(len(result_title),len(result_href),len(result_tag))
        for index,title in enumerate(result_title):
            news_dict = {}
            news_dict["title"] = title
            news_dict["url"] = result_href[index]
            news_dict["tag"] = result_tag[index]
            news_list.append(news_dict)
        print(news_list)
        return news_list

    # 保存数据
    def save_response(self,news):
        #将news_list转化成列表，然后以json格式保存
        # 调用json.dumps
        data = json.dumps(news)
        json.dump(news,open('4.json',"w",encoding="utf-8"))


    def run(self):
        data = ""
        # P12存在格式问题
        for page in range(1, 12):
            # 拼接完整url
            url = self.base_url + str(page)
            print(url)
            # 发送请求
            page_data = self.get_response(url)
            data += page_data

        for page in range(13, 24):
            # 拼接完整url
            url = self.base_url + str(page)
            print(url)
            # 发送请求
            page_data = self.get_response(url)
            data += page_data

        # 解析数据
        news_list = self.xpath_reponse(data)
        # 保存数据
        self.save_response(news_list)

Spider().run()