from selenium import webdriver
import time


def open_brower(type_):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    try:
        driver = getattr(webdriver, type_)(options=options)
    except:
        driver = webdriver.Chrome()
    return driver


class Keys:

    # 初始化
    def __init__(self, type_):
        self.driver = open_brower(type_)
        self.driver.implicitly_wait(5)

    # 打开网址
    def open(self, url):
        self.driver.get(url)

    # 输入文本
    def input(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)

    # 点击
    def click(self, by, value):
        self.driver.find_element(by, value).click()

    # 等待时间
    def wait(self, time_):
        time.sleep(time_)

    # 退出浏览器
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    key = Keys('Chrome')
    key.open('http://www.baidu.com')
    key.input('id', 'kw', '你好')
    key.click('id', 'su')
    key.wait(3)
    key.quit()