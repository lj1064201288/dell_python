import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Email = '1064201288@qq.com'
Password = 'liujun19960106'


class CrackGeetest(object):
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.email = Email
        self.password = Password
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)

    def __del__(self):
        self.browser.close()

    def get_geestest_button(self):
        '''
        获取初始化验证码的按钮
        :return:
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        获取验证码的位置
        :return: 验证码位置的元组
        """
        image = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = image.location
        size = image.size
        top, bottom, lift, right = location['y']