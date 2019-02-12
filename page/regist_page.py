from base.base_action import BaseAction
import page
class RegistPage(BaseAction):
    #1.初始化函数 传递driver
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #2.点击已有账号 去登录
    def  click_btn_already_account(self):
        self.click_element(page.aolai_regist_btn_already_account)
   