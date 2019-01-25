import urllib.parse
import urllib.request
import string

def get_search_result(keyword):

    url = "http://www.baidu.com/s?wd="
    request_url = urllib.parse.quote(url + keyword, safe=string.printable)

    print('搜索网页地址 -> ' + request_url)
    response = urllib.request.urlopen(request_url)
    print(response)
    #读取网页内容
    data = response.read().decode()
    print(data)

    #保存到本地
    with open('baidu_search.html', 'w', encoding='utf-8') as f:
        f.write(data)


get_search_result('美女')