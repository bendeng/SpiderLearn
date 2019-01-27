import urllib.parse
import urllib.request
import string
from http import cookiejar

def request_with_cookie():

    #先通过浏览器登陆谷歌账号，然后抓到ua和cookie，那么可以直接访问到登陆后的网页
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie':'HSID=A3il5xfAVlYv9k0UL; SSID=ATs5xEGhH1gUw1g7K; APISID=3CQt3zaoyQColdm8/Am97x_o4FsHpYfo7u; SAPISID=TavXzfb9DgINzkbK/A-SezUepFdxvp4iTb; SID=pQYRc5S6Zun3iVMbTmFWO4-Yvko1ya-pIJRz6ViOcDsPnNIvmJTNmo9vwIUXJjRdNUUJfA.; NID=156=YgLJpa7ZKWg2KWl6SU8TZKjk8VebQAPcslUfdDN77WgHGp8NYykhM6vbtOtFRLW7JsV2rVd4HEh3q27StJ4z34o8kK3tUPXt3mNS8bciFXr1NLf2D19IhXDJxijWLk69aQAtxzXNCmoGJUdqSICQjciWmJSfEnllZypZKoQL6MPb7z8QD5_TmtaSSgj6-SaOikV-NnF6MllEigEj_bmuMq_B-C-wsSRGossA4Q1O3n4vy7RY3V5IAMIMAkJcLnWY_MU; DV=M63v3DmUKlJbEC-3iDq2DVuy9JbZiBYvSfGgakooKQIAAOB65KG88IljsAAAAFisXfuWFXGaSQAAADQKmJDzn0kTFAAAAA; 1P_JAR=2019-1-27-4; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTU0ODU2Mzg3Mzk4NzAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6MTM3NzQ2MzMxIGxvbmdpdHVkZV9lNzoxMDA1NzM0MzE1fSByYWRpdXM6NDE1NDA=; SIDCC=ABtHo-GFWhypCDcKrT1SuQfnLTPmAd5u-VwdWLYiUEBfH44EOUEJYqqIIIR3NCnV3MfK02lgJh8'
    }

    url = "https://www.google.com"
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

    #打印完整的请求头信息
    print(request.headers)

    # 保存到本地
    with open('google_cookie.html', 'w', encoding='utf-8') as f:
        f.write(data)


def login_with_code():
    # 1. 代码登录
    # 1.1 登录的网址
    login_url = 'https://www.yaozh.com/login'
    # 1.2 登录的参数
    login_form_data = {
        "username": "xiaomaoera12",
        "pwd": "lina081012",
        "formhash": "CE3ADF28C5",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"

    }
    # 1.3 发送登录请求POST
    cook_jar = cookiejar.CookieJar()
    # 定义有添加  cook 功能的 处理器
    cook_hanlder = urllib.request.HTTPCookieProcessor(cook_jar)
    # 根据处理器 生成 opener
    opener = urllib.request.build_opener(cook_hanlder)

    # 带着参数 发送post请求
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    # 1.参数 将来 需要转译 转码; 2. post请求的 data要求是bytes
    login_str = urllib.parse.urlencode(login_form_data).encode('utf-8')

    login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
    # 如果登录成功, cookjar自动保存cookie
    opener.open(login_request)

    # 2. 代码带着cooke去访问 个人中心
    center_url = 'https://www.yaozh.com/member/'
    response = opener.open(center_url)
    # bytes -->str
    data = response.read().decode()

    with open('cookie.html', 'w') as f:
        f.write(data)

try:
    login_with_code()
except urllib.request.HTTPError as httpError:
    print(httpError.code)
except urllib.request.URLError as urlError:
    print(urlError.reason)


