#https://www.baidu.com/s?wd=虎扑
import urllib.request
import ssl
#可以利用以下两个库进行转译
import urllib.parse
import string

def get_method_params():
    url = "https://www.baidu.com/s?wd="

    # 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    # python属于解释行语言；解析器只支持ASCII
    # 因此，需要利用将其中文转译
    name = "虎扑"
    final_name = url + name
    # 转译
    new_final_name = urllib.parse.quote(final_name, safe=string.printable)
    print(final_name)
    print(new_final_name)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(new_final_name, context=context)
    print(response)
    response_data = response.read()

    str_response = response_data.decode("utf-8")

    with open("hupu.html","w",encoding="utf-8") as f:
        f.write(str_response)

get_method_params()

