from urllib import request
import urllib.parse
import json
# 利用又到词典去
# url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
header={
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://fanyi.youdao.com"
}

data={
    "i":"desperate",
    "from":"en",
    "to":"zh-CHS",
    "smartresult":    "dict",
    "client":"fanyideskweb",
    "salt":    "15919709230855",
    "sign":"e0bf22d1ea048abd91fd7e2c48a09938",
    "ts":"1591970923085",
    "bv":"3c9654c6f607aca442ac5f0c0528095f",
    "doctype":    "json",
    "version":    "2.1",
    "keyfrom":    "fanyi.web",
    "action":"FY_BY_REALTlME"
}

# 把data转为字符串，再把其变成二进制形式
datas = urllib.parse.urlencode(data).encode('utf-8')
request = request.Request(url,data=datas,headers=header)
repsonse = urllib.request.urlopen(request)
str_repsonse  = repsonse.read().decode("utf-8")
print(str_repsonse)
a = json.loads(str_repsonse)
print(a['translateResult'][0][0]['tgt'])