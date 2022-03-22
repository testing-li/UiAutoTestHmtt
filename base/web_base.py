from time import sleep
from base.base import Base
from selenium.webdriver.common.by import By


class WebBase(Base):
    """以下为web项目专属方法"""

    # 根据显示文本点击指示元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1.点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2.暂停
        sleep(1)
        # 3.点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)
