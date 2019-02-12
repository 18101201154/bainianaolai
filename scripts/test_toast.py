import os,sys
import pytest
sys.path.append(os.getcwd())
import page
import time
from page.navigation_page import NavigationPage
from base.init_driver import get_driver
from base.read_yaml import read_yaml_data

def get_test_login_data():
    data_list = []
    login_data = read_yaml_data("login_data.yaml")
    for i in login_data.keys():
        username = login_data.get(i).get("username")
        password = login_data.get(i).get("password")
        data_list.append((username, password))
    return data_list

class TestLogin:
    #在测试函数之前执行
    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.aolai_app_package,page.aolai_app_activity)
        #2.初始化导航类
        self.navigation_page = NavigationPage(self.driver)

    #最后执行
    def teardown_class(self):
         #关闭driver
         self.driver.quit()

    #测试函数
    @pytest.mark.parametrize("username,password",get_test_login_data())
    def test_login(self,username,password):
        #1.点击我的
        self.navigation_page.get_home_page_obj().click_btn_my()
        #2.点击已有账号 去登录
        self.navigation_page.get_regist_page_obj().click_btn_already_account()
        #3 输入账号密码 登录
        self.navigation_page.get_login_page_obj().click_btn_login(username,password)
        #4.获取toast的内容 通过xpath定位
        toast_msg = self.navigation_page.get_login_page_obj().find_element(page.aolai_toast_pwd_error).text
        print(toast_msg)







