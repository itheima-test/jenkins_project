import time
import pytest
import allure
from allure_commons.types import AttachmentType

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, args):

        # 解析 yaml 的数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 脚本流程
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        allure.attach(self.driver.get_screenshot_as_png(),name="图片", attachment_type=allure.attachment_type.PNG)
        self.page.login.click_login()

        if toast is None:
            assert self.page.me.get_nick_name_text() == username, "登录后的用户名和输入的用户民不一致"
        else:
            # 找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.login.is_toast_exist(toast)
