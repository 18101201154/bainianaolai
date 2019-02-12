from base.base_action import BaseAction
import page
class LoginPage(BaseAction):
    #1.初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)



    #2 实现登录逻辑
    def click_btn_login(self,username,password):
        #2.1 输入账号
        self.input_edit_content(page.aolai_login_edit_account,username)
        #2.2 输入密码
        self.input_edit_content(page.aolai_login_edit_password,password)
        #2.3 点击登录
        self.click_element(page.aolai_login_btn_login)

    #3 点击关闭登录页面的功能
    def click_close_login_page(self):
        self.click_element(page.aolai_login_btn_close_login)

