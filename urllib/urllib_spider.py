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


def load_data_by_proxy_ip():
    url = "http://www.baidu.com"
    # handler = urllib.request.HTTPHandler()
    # opener = urllib.request.build_opener(handler)
    # response = opener.open(url)
    # data = response.read().decode()
    # print(data)

    #添加代理
    proxy = {
        #网上找的免费代理IP写法
        #"http":"180.118.86.26"
        #"http":"http://180.118.86.26",
        #付费的代理ip,第一种写法
        "http":"username:pwd@180.118.86.26"
    }

    #代理ip池
    proxies = [
        proxy,
        { "http":"http://115.213.243.225" },
        { "http":"http://183.129.244.16" },
        { "http":"http://144.255.13.171" }
    ]

    #代理ip就不用随机了，有可能几次用的是一样的
    for pro in proxies:
        # 创建代理handler
        proxyHandler = urllib.request.ProxyHandler(pro)
        proxyOpener = urllib.request.build_opener(proxyHandler)

        try:
            # 使用代理ip发送请求
            response = proxyOpener.open(url)
            #print(response.header)
            data = response.read().decode()
            #print(data)
        except Exception as e:
            print(e)


def money_proxy_ip():
    url = ""
    username = ""
    password = ""
    proxyip = ""
    #使用密码管理器，添加用户名密码。这种方式有个好处就是一个用户名下多个代理ip很方便，不用像第一种方式要拼接
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None,proxyip, username,password)
    #创建验证代理ip的处理器
    handler_auth_proxy = urllib.request.ProxyBasicAuthHandler()
    #下面两步就是发送请求
    opener_auth = urllib.request.build_opener(handler_auth_proxy)
    opener_auth.open(url)

#访问内网去获取数据
def auth_nei_wang():
    #1.用户名密码
    user = "admin"
    pwd = "adimin123"
    nei_url = "http://192.168.0.66"


    #2.创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    pwd_manager.add_password(None,nei_url,user,pwd)

    #创建认证处理器(requests)
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    opener = urllib.request.build_opener(auth_handler)

    response = opener.open(nei_url)
    print(response)

#get_search_result('美女')
#get_search_result_by_mutiple_params()
#get_search_result_modify_ua()
load_data_by_proxy_ip()