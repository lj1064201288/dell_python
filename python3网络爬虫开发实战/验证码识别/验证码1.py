from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

Email = '1064201288@qq.com'
Password = 'liujun19960106'

class CrackGeetest():
    # 初始化
    def __init__(self):
        self.url = "https://account.geetest.com/login/"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = Email
        self.password = Password
    # 模拟点击
    def get_geetest_button(self):
        '''
        获取初始验证按钮
        :return:
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_btn')))
        return  button


button = CrackGeetest()
button.browser.get(button.url)
buttom = button.get_geetest_button()
buttom.click()