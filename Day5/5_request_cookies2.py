import requests

# 1.利用代码登陆
# 2.利用cookies登陆
login_url = "https://www.yaozh.com/login/"
member_url = "https://www.yaozh.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

login_form_data = {
    "username": "15871688074",
    "pwd": "xin665968",
    "formhash": "768736467D",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}
session = requests.session()

# 此处，再用cookie方法去获取cookies较为繁琐
# 因此，新方法session 类 可以自动保存cookies

login_response = session.post(login_url,headers=headers,data=login_form_data)
member_response = session.get(member_url,headers=headers).content.decode("utf-8")
print(member_response)

with open("5.html","w",encoding="utf-8") as f:
    f.write(member_response)