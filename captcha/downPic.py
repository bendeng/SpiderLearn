import requests

# 中国知网的登录验证码地址
url = 'http://login.cnki.net/login/checkcode.aspx'

def download_save_pic(index):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.content)
    with open('img/code_' + str(index) + '.png','wb') as f:
        for data in response.iter_content(128):
            f.write(data)
        f.close()


if __name__ == '__main__':
    for i in range(1,11):
        download_save_pic(i)

