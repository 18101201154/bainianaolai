import page
from base.base_action import BaseAction


class AddressGuanliPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    # 点击新增地址
    def click_btn_add_address_guanli(self):
        self.click_element(page.aolai_address_guanli_add_btn)
    # 点击编辑
    def click_text_bianji_guanli(self):
        self.click_element(page.aolai_address_guanli_bianji_text)
    # 点击修改按钮
    def click_btn_updata_addressguanli(self):
        self.click_element(page.aolai_address_guanli_updata_btn)
    # 点击删除按钮
    def click_btn_del_address_guanli(self):
        self.click_element(page.aolai_address_guanli_del_btn)
    # 点击保存
    def click_btn_save_address_guanli(self):
        self.click_element(page.aolai_address_guanli_save_btn)
