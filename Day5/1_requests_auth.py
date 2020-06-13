# 利用requests发送post请求
import requests
url = "https://printaccount.ucl.ac.uk/safecom"
# 发送post请求

user="uczlhg6"
pwd="XIN_665968"
data={}
# 需要传入元祖形式
auth = (user,pwd)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
response = requests.post(url, headers=headers,data=data,auth=auth)
str_response = response.content.decode("utf-8")
with open("1.html","w",encoding="utf-8") as f:
    f.write(str_response)