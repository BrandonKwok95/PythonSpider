import requests


login_url = "https://www.yaozh.com/member"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

cookies = "PHPSESSID=ok2neunss1fohsg7n7ndbn0da2; _ga=GA1.2.990699265.1591866172; UtzD_f52b_saltkey=lnZkHnMR; UtzD_f52b_lastvisit=1591862660; _gid=GA1.2.480783490.1591974277; _pk_ref.6.c32b=%5B%22%22%2C%22%22%2C1591989831%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D; _pk_ses.6.c32b=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1591989836; yaozh_userId=939291; yaozh_uidhas=1; yaozh_mylogin=1591990119; _pk_ref_5_c4a6=%5B%22%22%2C%22%22%2C1591862772%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1591862772%2C1591866173; _pk_id_5_c4a6=84b060d5d3c7e2fb.1591862772.1.1591866267.1591862772.; acw_tc=2f624a4415919898293814110e2c4f2482ff4035bb66d1797562844e762caf; _pk_ref_6_c32b=%5B%22%22%2C%22%22%2C1591989831%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D; _pk_ses_6_c32b=1; _pk_id_6_c32b=12de3ef54a07cecc.1591862777.3.1591989836.1591989831.; _pk_id_6_c4a6=a023ec44e71aa391.1591991088.1.1591991088.1591991088.; _pk_ses_6_c4a6=1; _pk_id.6.c4a6=a023ec44e71aa391.1591991088.1.1591991094.1591991088.; _ga=GA1.1.241633062.1591991094; _gid=GA1.1.946951303.1591991094; UtzD_f52b_ulastactivity=1591862871%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D789462; UtzD_f52b_creditbase=0D0D2D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _gat=1; _pk_ref.5.c4a6=%5B%22%22%2C%22%22%2C1591992339%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D; _pk_ses.5.c4a6=1; yaozh_user=939291%09%E4%BC%A6%E6%95%A6%E7%A7%BB%E5%8A%A8U%E7%9B%98; db_w_auth=789462%09%E4%BC%A6%E6%95%A6%E7%A7%BB%E5%8A%A8U%E7%9B%98; _pk_ses_5_c4a6=1; yaozh_logintime=1591993402; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaaap5nnpWHnKZxanJT1qeSoMZYoNdzaJdyVEchCEf5CkjeIBrvDLpIzs9Xc6SbcmtVzZfY2JiryqWXhaD91f6a625e4f1920ad4170D2E67C01D04Vm5WUm1mWap6VnppmamptU5ysa2ebWNnNppyDc6WdlpWbhpWWcJZunpeZkWZpaHBTnLY%3D4e24f15ee593b0dd1a4d9b0197163c8b; UtzD_f52b_lastact=1591993404%09uc.php%09; UtzD_f52b_auth=0fe7XDRlV2C2k38JLMSqLBP3gPilDqBaP%2BzYCalu3UetwzvIbstiv6Y2POu72yRqz9vx74VjYw8jgAZEDBhlJB4l%2Bn0; _pk_id.5.c4a6=84b060d5d3c7e2fb.1591862772.2.1591993654.1591992339.; _pk_id.6.c32b=12de3ef54a07cecc.1591862777.3.1591993738.1591989831."# Cookies是字典或cookiejar的形式

# 此处利用字典传入，较为繁琐
# i.学会用sublime text用正则式替换
"""
cookies_dir = {
    "_pk_ref.5.c4a6": "%5B%22%22%2C%22%22%2C1591862772%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D",
    "PHPSESSID": "ok2neunss1fohsg7n7ndbn0da2",
    "_ga": "GA1.2.990699265.1591866172",
    "UtzD_f52b_saltkey": "lnZkHnMR",
    "UtzD_f52b_lastvisit": "1591862660",
    "_pk_id.5.c4a6": "84b060d5d3c7e2fb.1591862772.1.1591866267.1591862772.",
    "_gid": "GA1.2.480783490.1591974277",
    "acw_tc": "2f624a4415919898293814110e2c4f2482ff4035bb66d1797562844e762caf",
    "_pk_ref.6.c32b": "%5B%22%22%2C%22%22%2C1591989831%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D",
    "_pk_ses.6.c32b": "1",
    "Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94": "1591989836",
    "yaozh_logintime": "1591990116",
    "yaozh_user": "939291%09%E4%BC%A6%E6%95%A6%E7%A7%BB%E5%8A%A8U%E7%9B%98",
    "yaozh_userId": "939291",
    "yaozh_jobstatus": "kptta67UcJieW6zKnFSe2JyXnoaaap5nnpWHnKZxanJT1qeSoMZYoNdzaJdyVEchCEf5CkjeIBrvDLpIzs9Xc6SbcmtVzZfY2JiryqWXhaD5A64aBE6391b127FE8d2F7683C52df6BVm5WUm1mWap6VnZdpaGpuU5ysa2ebWNnNppyDc6WdlpWbhpWWcJZunpSWkmppbG5TnLY%3D9cea56ce7127256ff2d9d09916de1e15",
    "db_w_auth": "789462%09%E4%BC%A6%E6%95%A6%E7%A7%BB%E5%8A%A8U%E7%9B%98",
    "UtzD_f52b_lastact": "1591990118%09uc.php%09",
    "UtzD_f52b_auth": "205fz2KPv2WnUrBgkofqLhVOp2PfMb6lbtr9Ige2NVPZRfrgle%2BBJK0pqgR08NUbtaqYpH%2BdYVoDRC9agACboAbVj2M",
    "yaozh_uidhas": "1",
    "yaozh_mylogin": "1591990119",
    "_pk_ref_5_c4a6": "%5B%22%22%2C%22%22%2C1591862772%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1svmmlHDbT6cM84tqz0iXvOW8DIY-Nfbtadhee4rTIO%26wd%3D%26eqid%3Db02299460000cffd000000065ee1e5ec%22%5D",
    "Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94": "1591862772%2C1591866173",
    "_pk_id_5_c4a6": "84b060d5d3c7e2fb.1591862772.1.1591866267.1591862772.",
    "acw_tc": "2f624a4415919898293814110e2c4f2482ff4035bb66d1797562844e762caf",
    "_pk_ref_6_c32b": "%5B%22%22%2C%22%22%2C1591989831%2C%22https%3A%2F%2Fwww.yaozh.com%2F%22%5D",
    "_pk_ses_6_c32b": "1",
    "_pk_id_6_c32b": "12de3ef54a07cecc.1591862777.3.1591989836.1591989831.",
    "_pk_id.6.c32b": "12de3ef54a07cecc.1591862777.3.1591990122.1591989831."
}
response = requests.get(login_url,headers=headers,cookies=cookies_dir)
data = response.content.decode("utf-8")
with open("4_1.html","w",encoding="utf-8") as f:
    f.write(data)"""

# ii.利用split函数拆分字符串***重要
cookies_list = cookies.split("; ")
cookies_dict = {}
for cook in cookies_list:
    cookies_dict[cook.split("=")[0]] = cook.split("=")[1]
print(cookies_dict)
# 也可以达到上述语句效果（字典推导式）
# cookies_dict = {cook.split("=")[0]:cook.split("=")[1] for cook in cookies.split("; ")}
response = requests.get(login_url,headers=headers,cookies=cookies_dict)
data = response.content.decode("utf-8")
with open("4_2.html","w",encoding="utf-8") as f:
    f.write(data)