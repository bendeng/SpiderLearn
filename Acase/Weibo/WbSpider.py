from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from DB import DB,DbType



class WeiboSpider:

    def __init__(self):
        print('调用构造函数\n')
        self.url = 'https://www.weibo.com/dengpan22?is_all=1'

    def __del__(self):
        print('\n对象不再使用，析构')

    def start(self):
        print('开始抓取微博内容')
        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        driver = webdriver.Chrome(
            executable_path='./chromedriver',
            options=option
        )

        # 打开网站
        driver.get(self.url)

        # 等待网页加载完成
        timeout = 30
        wb_content = WebDriverWait(driver, timeout).until(
            lambda e: e.find_elements_by_xpath('//div[@class="WB_text W_f14"]'))

        if len(wb_content) > 0:
            data = []
            for wb_item in wb_content:
                #print(wb_item.text)
                data.append({'content':wb_item.text})

            self.save(data)

    def save(self, data):
        db = DB()
        db.save(DbType.MONGO, data)




if __name__ == '__main__':
    wbspider = WeiboSpider()
    wbspider.start()