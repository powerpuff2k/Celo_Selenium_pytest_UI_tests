from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.PinSetupPage import PinSetUpPage
import pytest


class Helpers(BasePage):
    """By locators"""
    NAV_MENU = (By.ID, "nav-menu")
    LOGOUT_BUTTON = (By.ID, "celo-logout-button")
    LOGIN_LINK = (By.ID, "login")
    EMAIL = (By.ID, "Username")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.NAME, "button")


    """Constructor for page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """Page actions"""

    """To login"""

    def do_login(self, username, password):
        self.do_click(self.LOGIN_LINK)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return PinSetUpPage(self.driver)

    """To Logout"""
    def logout(self):
        self.do_click(self.NAV_MENU)
        self.do_click(self.LOGOUT_BUTTON)

