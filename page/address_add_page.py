import page
from base.base_action import BaseAction


class AddressAddPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    def click_add_address_save_btn(self,reciver,phone,city,city1,post,morenaddress):
#       输入收件人
        self.input_edit_content(page.aolai_add_address_reciver,reciver)
#       输入手机号
        self.input_edit_content(page.aolai_add_address_tel,phone)
#       输入所在地址
        self.input_edit_content(page.aolai_add_address_city,city)
#       输入详细地址
        self.input_edit_content(page.aolai_add_address_xiangxi_address,city1)
#       邮编
        self.input_edit_content(page.aolai_add_address_post,post)
#       设为默认地址
        self.input_edit_content(page.aolai_add_address_morenaddress,morenaddress)
#       点击保存
        self.click_element(page.aolai_add_address_save_btn)