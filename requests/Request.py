import requests

# 发送post请求
# data = {
#
# }
# response = requests.post(url, data=data)


# 内网 需要 认证
# auth = (user,pwd)
# response = requests.get(url,auth=auth)

#代理IP请求
def request_with_proxy():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

    free_proxy = {'http': '27.17.45.90:43411'}

    response = requests.get(url=url, headers=headers, proxies=free_proxy)

    print(response.status_code)


def request_with_cookie():
    # 请求数据url
    member_url = 'https://www.yaozh.com/member/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    #  cookies 的字符串
    cookies = '_ga=GA1.2.1820447474.1535025127; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=70kadg2ahpv7uuc8docd09iat4; _gid=GA1.2.133568065.1540383729; _gat=1; MEIQIA_VISIT_ID=1C1OdtdqpgpGeJ5A2lCKLMGiR4b; yaozh_logintime=1540383753; yaozh_user=381740%09xiaomaoera12; yaozh_userId=381740; db_w_auth=368675%09xiaomaoera12; UtzD_f52b_saltkey=ylH82082; UtzD_f52b_lastvisit=1540380154; UtzD_f52b_lastact=1540383754%09uc.php%09; UtzD_f52b_auth=f958AVKmmdzQ2CWwmr6GMrIS5oKlW%2BkP5dWz3SNLzr%2F1b6tOE6vzf7ssgZDjhuXa2JsO%2FIWtqd%2FZFelWpPHThohKQho; yaozh_uidhas=1; yaozh_mylogin=1540383756; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1535025126%2C1535283389%2C1535283401%2C1539351081%2C1539512967%2C1540209934%2C1540383729; MEIQIA_VISIT_ID=1C1OdtdqpgpGeJ5A2lCKLMGiR4b; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540383761'

    # 需要的是 字典类型
    cook_dict = {}
    cookies_list = cookies.split('; ')
    for cookie in cookies_list:
        cook_dict[cookie.split('=')[0]] = cookie.split('=')[1]

    # 字典推导式
    cook_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}

    response = requests.get(member_url, headers=headers, cookies=cook_dict)

    data = response.content.decode()

    with open('05-cookie.html', 'w') as f:
        f.write(data)



def request_with_cookie2():
    import requests

    # 请求数据url
    member_url = 'https://www.yaozh.com/member/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    # session 类 可以自动保存cookies === cookiesJar
    session = requests.session()
    # 1.代码登录
    login_url = 'https://www.yaozh.com/login'
    login_form_data = {
        'username': 'xiaomaoera12',
        'pwd': 'lina081012',
        'formhash': '54AC1EE419',
        'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F',
    }
    login_response = session.post(login_url, data=login_form_data, headers=headers, verify=False)
    print(login_response.content.decode())
    # 2.登录成功之后 带着 有效的cookies 访问 请求目标数据
    data = session.get(member_url, headers=headers).content.decode()

    with open('05-cookie2.html', 'w') as f:
        f.write(data)


request_with_cookie2()


