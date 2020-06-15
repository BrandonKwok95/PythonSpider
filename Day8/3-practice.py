from lxml import etree
import requests
import json
import csv
from bs4 import BeautifulSoup
import re

class Spider_3rd(object):
    def __init__(self):
        self.base_url = "http://www.allitebooks.org/page/"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }
    # 获取数据
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        str_response = response.content.decode("utf-8")
        return str_response

    # 解析数据
    def parse_response(self, response):
        xpath_response = etree.HTML(response)
        soup = BeautifulSoup(response, 'lxml')
        # 书本图片
        # class ="attachment-post-thumbnail wp-post-image"
        result_image = xpath_response.xpath('//img[@class="attachment-post-thumbnail wp-post-image"]/@src')
        # 书本链接
        result_link = xpath_response.xpath('//header[@class="entry-header"]//a[@rel="bookmark"]/@href')
        # 书本作者
        result_author = xpath_response.xpath('.//h5[@class="entry-author"]//text()')
        print(result_author)
        result_string = ""
        for string in result_author:
            result_string += string
        print(result_string)
        print(type(result_string))
        # 利用正则表达式根据By: 将其切开
        pattern = re.compile('By: ')
        result_author = pattern.split(result_string)
        result_author.pop(0)
        print(result_author)
        print(len(result_author))

        """第二种方法（加载到网页查看速度较慢）
        result_author = []
        for link in result_link:
            link_response = self.get_response(link)
            xpath_link = etree.HTML(link_response)
            author_link = xpath_link.xpath('//dd//a[@rel="tag"]/text()')
            result_author.append(author_link)"""
        # 书本标题
        result_title = xpath_response.xpath('//h2[@class="entry-title"]//a[@rel="bookmark"]/text()')
        books_list = []
        for index,link in enumerate(result_link):
            book_dict ={}
            book_dict['link'] = link
            book_dict['title'] = result_title[index]
            book_dict['img'] = result_image[index]
            book_dict['authors'] = result_author[index]
            books_list.append(book_dict)
            print(book_dict)
        return books_list

    #保存相关数据
    def save_response(self,news):
        #将news_list转化成字符串，然后以json格式保存
        # 调用json.dumps
        data = json.dumps(news)
        json.dump(news,open('3.json',"w",encoding="utf-8"))

    def save_csv(self, data_list):
        sheet_title = data_list[0].keys()
        sheet_data = []
        for data in data_list:
            sheet_data.append(data.values())
        writer = csv.writer(open('3.csv', 'w'))
        writer.writerow(sheet_title)
        writer.writerows(sheet_data)

    def run(self):
        total_books = []
        for page in range(1, 16):
            str_response = self.get_response('http://www.allitebooks.org/page/'+str(page))
            books_list = self.parse_response(str_response)
            total_books += books_list
        self.save_response(total_books)
        print(total_books)
        self.save_csv(total_books)

Spider_3rd().run()