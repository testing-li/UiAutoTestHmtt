from selenium import webdriver


class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空（多次调用，确保返回的是同一个对象）
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)
        # 不为空，返回driver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None