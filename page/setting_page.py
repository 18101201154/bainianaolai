from base.base_action import BaseAction
import page
import time
class SettingPage(BaseAction):
    #1.初始化函数
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #2.退出登录
    def click_setting_btn_logout(self):
        #2.1 让页面滑动底部
        self.swipe_screen(1)
        time.sleep(1)
        #2.2 点击退出按钮
        self.click_element(page.aolai_setting_btn_setting_logout)
        #2.3 点击 对话框 确认按钮
        self.click_element(page.aolai_setting_btn_dialog_confirm)
    def click_guanli_address(self):
        # 点击地址管理
        self.click_element(page.aolai_setting_btn_guanli_address)

