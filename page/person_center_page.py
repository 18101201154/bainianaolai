from base.base_action import BaseAction
import page
class PersonCenterPage(BaseAction):
    #1.实现初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #2.点击左上角设置按钮
    def click_btn_left_setting(self):
        self.click_element(page.aolai_person_center_btn_left_setting)