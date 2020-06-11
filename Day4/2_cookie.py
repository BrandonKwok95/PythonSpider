# 设置cookies
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# 可以看出未添加cookies时候，网页显示未登录
def cookies_use():
    url = "https://www.yaozh.com/member"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        # 添加cookie可以获取用户信息（购物车）
        "Cookie": "acw_tc=2f624a0b15918627669432123e0f3b0b6edd9f2cb91979b5150f3fd026eb2c; PHPSESSID=bbdt93s7loc6b1k7cf03j6n7p4; _ga=GA1.2.3232058.1591862770; _gid=GA1.2.1768305940.1591862770; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1591862772; _pk_ref.5.c4a6=%5B%22%22%2C%22%22%2C1591862772%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D; _pk_ses.5.c4a6=1; _pk_ref.6.c32b=%5B%22%22%2C%22%22%2C1591862777%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D; _pk_ses.6.c32b=1; yaozh_logintime=1591862871; yaozh_user=939291%09%E4%BC%A6%E6%95%A6%E7%A7%BB%E5%8A%A8U%E7%9B%98; yaozh_userId=939291; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaaap5nnpWHnKZxanJT1qeSoMZYoNdzaJdyVEchCEf5CkjeIBrvDLpIzs9Xc6SbcmtVzZfY2JiryqWXhaD0f92881858E7a3cd9CC344C9d6c04212Vm5WUm1mWap6VnZdlb2xpU5ysa2ebWNnNppyDc6WdlpWbhpWWcJZtm5admGZuZm9TnLY%3D12b52728c02893eb7d65cf57aa1c1141; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1591862875; _pk_id.6.c32b=12de3ef54a07cecc.1591862777.1.1591862875.1591862777.; yaozh_uidhas=1; yaozh_mylogin=1591862878; acw_tc=2f624a0b15918627669432123e0f3b0b6edd9f2cb91979b5150f3fd026eb2c; _pk_ref_5_c4a6=%5B%22%22%2C%22%22%2C1591862772%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D; _pk_id_5_c4a6=84b060d5d3c7e2fb.1591862772.1.1591862772.1591862772.; _pk_ses_5_c4a6=1; _pk_ref_6_c32b=%5B%22%22%2C%22%22%2C1591862777%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D; _pk_ses_6_c32b=1; _pk_id_6_c32b=12de3ef54a07cecc.1591862777.1.1591862875.1591862777.; _pk_id.5.c4a6=84b060d5d3c7e2fb.1591862772.1.1591862908.1591862772."
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    str_response = response.read().decode("utf-8")
    with open("2.html", "w", encoding="utf-8") as f:
        f.write(str_response)


cookies_use()