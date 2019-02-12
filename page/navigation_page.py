from page.address_add_page import AddressAddPage
from page.address_guanli_page import AddressGuanliPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.regist_page import RegistPage
from page.setting_page import SettingPage
"""
导航类 这个类负责初始化其他几个类的实例 
只要获取导航类的实例 就可以获取其他几个类的实例  
"""
class NavigationPage:
    def __init__(self,driver):
        self.driver = driver

    #获取homepage的实例
    def get_home_page_obj(self):
        return HomePage(self.driver)

    #获取登录页面的实例
    def get_login_page_obj(self):
        return LoginPage(self.driver)

    # 获取个人中心的实例
    def get_person_center_obj(self):
        return PersonCenterPage(self.driver)

    # 获取注册页面的实例
    def get_regist_page_obj(self):
        return RegistPage(self.driver)

    # 获取设置页面的实例
    def get_setting_page_obj(self):
        return SettingPage(self.driver)

    # 获取地址管理页面实例
    def get_address_guanli_page_obj(self):
        return AddressGuanliPage(self.driver)

    #获取新增地址页面实例
    def get_address_add_page_obj(self):
        return AddressAddPage(self.driver)
#


