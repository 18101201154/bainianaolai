import pytest

import page
from base.init_driver import get_driver
from base.read_yaml import read_yaml_data
from page.navigation_page import NavigationPage

def get_test_address_data():
    address_list=[]
    address_expect_list=[]
    address_data=read_yaml_data("address_data.yaml")
    for i in address_data.keys():
        reciver=address_data.get(i).get("reciver")
        phone = address_data.get(i).get("phone")
        city1 = address_data.get(i).get("city1")
        post = address_data.get(i).get("post")
        tage= address_data.get(i).get("tage")
        expect_data=address_data.get(i).get("expect_data")
        address_list.append((reciver,phone,city1,post,tage,expect_data))
        # 获取异常信息expect_data,添加到列表中
        address_expect_list.append(expect_data)
    return address_list,address_expect_list

class TestAddress():
    def setup_class(self):
        # 初始化driver
        self.driver=get_driver(page.aolai_app_package,page.aolai_app_activity)
        # 初始化导航类
        self.navigation_page=NavigationPage(self.driver)
    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("reciver,phone,city,city1,post,tage")
    def test_address(self,reciver,phone,city,city1,post,tage):
        # 点击新增地址
        self.navigation_page.get_address_add_page_obj()
        # 输入收件人,输入手机号,所在地区,详细地址, 邮编,设为默认地址
        self.navigation_page.get_address_add_page_obj().click_add_address_save_btn(reciver,phone,city,city1,post)
        #通过自定义的tag进行预期成功和失败判断
        if tage==1:
            try:
#                 跳转到地址管理-新增地址
                self.navigation_page.get_address_guanli_page_obj().click_text_bianji_guanli()
            except Exception:
                #出现异常,实现截图
                self.navigation_page.get_address_guanli_page_obj().get_screen()
        else:
            toast_msg=self.navigation_page.get_address_guanli_page_obj().find_element(page.aolai_toast_reciver_error).text



