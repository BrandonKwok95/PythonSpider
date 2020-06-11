# http错误
import urllib.request

url = "https://www.dsadsadssssdsdsa.com/"
response = urllib.request.urlopen(url)
# 应当利用try...except，防止报错，并返回会相关的错误信息