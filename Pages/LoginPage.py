from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.PinSetupPage import PinSetUpPage
import pytest


class LoginPage(BasePage):
    """By locators"""
    LOGIN_LINK = (By.ID, "login")
    EMAIL = (By.ID, "Username")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.NAME, "button")

    """Constructor for page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""

    """To get title"""
    def get_page_title(self, title):
        return self.get_title(title)

    """Check if login link exists"""
    def is_login_link_exist(self):
        return self.is_visible(self.LOGIN_LINK)

    """Click login link"""
    def click_login(self):
        self.do_click(self.LOGIN_LINK)

    def do_login(self, username, password):
        self.do_click(self.LOGIN_LINK)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return PinSetUpPage(self.driver)
