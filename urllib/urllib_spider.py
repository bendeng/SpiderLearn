import urllib.parse
import urllib.request
import string
import random

#urllib是python3原生自带的
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


#urllib请求采用多参数的模式
def get_search_result_by_mutiple_params():

    params = {
        'wd':'美女',
        'key':'key',
        'value':'value'
    }

    #urllib.parse.urlencode可以将字典翻译成字符串key=value的形式
    str_params = urllib.parse.urlencode(params);
    print(str_params)
    url = "http://www.baidu.com/s?"
    request_url = urllib.parse.quote(url + str_params, safe=string.printable)

    print('搜索网页地址 -> ' + request_url)
    response = urllib.request.urlopen(request_url)
    print(response)
    #读取网页内容
    data = response.read().decode()
    print(data)

    #保存到本地
    with open('baidu_search.html', 'w', encoding='utf-8') as f:
        f.write(data)



def get_search_result_modify_ua():

    #User-Agent列表，请求时随机一个，让服务器不要认为我们是爬虫
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    ]

    header = {
        #随机一个UA
        'User-Agent': random.choice(user_agent_list),
        'h_key':'key',
        'h_val':'value'
    }

    url = "http://www.baidu.com/s?wd=美女"
    #UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    request_url = urllib.parse.quote(url, safe=string.printable)
    #创建请求对象
    request = urllib.request.Request(request_url, headers=header)
    response = urllib.request.urlopen(request)
    #查看响应头信息
    print(response.headers)
    # 读取网页内容
    data = response.read().decode()
    #print(data)

    #完整的url
    print('完整url = ' + request.get_full_url())
    #打印完整的请求头信息
    print(request.headers)

    # 保存到本地
    #with open('baidu_search.html', 'w', encoding='utf-8') as f:
        #f.write(data)


#get_search_result('美女')
#get_search_result_by_mutiple_params()
get_search_result_modify_ua()