from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class AboutPage(BaseAction):

    # 版本更新 按钮
    update_button = By.XPATH, "//*[@text='版本更新']"

    # 点击 版本更新
    @allure.step(title='关于百年奥莱 点击 更新版本')
    def click_update(self):
        self.click(self.update_button)

