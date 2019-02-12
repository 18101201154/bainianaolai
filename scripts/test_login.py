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
        tag = login_data.get(i).get("tag")
        expect_data = login_data.get(i).get("expect_data")
        data_list.append((username, password,tag,expect_data))
    print(data_list)
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
    @pytest.mark.parametrize("username,password,tag,expect_data",get_test_login_data())
    def test_login(self,username,password,tag,expect_data):
        #1.点击我的
        self.navigation_page.get_home_page_obj().click_btn_my()
        #2.点击已有账号 去登录
        self.navigation_page.get_regist_page_obj().click_btn_already_account()
        #3 输入账号密码 登录
        self.navigation_page.get_login_page_obj().click_btn_login(username,password)

        #4 通过我们自定义的tag 进行预期成功 和失败判断
        if tag == 1:
            try:
                # 4.跳转到个人中心 点击个人中心的左上角的设置按钮
                self.navigation_page.get_person_center_obj().click_btn_left_setting()
                # 5.实现滑动 点击退出 在点击确认对话框
                self.navigation_page.get_setting_page_obj().click_setting_btn_logout()
            except Exception:
                #6.当出现异常的情况 实现截图操作
                self.navigation_page.get_setting_page_obj().get_screen()
        else:

            #7.获取到弹出toast内容 应该是预期结果和实际的结果做对比
            toast_msg = self.navigation_page.get_setting_page_obj().find_element(page.aolai_toast_pwd_error).text
            #8.判断预期结果和实际结果是否一致
            assert  toast_msg == expect_data,self.navigation_page.get_setting_page_obj().get_screen()
            #9.关闭当前登录页面
            self.navigation_page.get_login_page_obj().click_close_login_page()






