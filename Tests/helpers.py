import pytest
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.Helpers import Helpers
from Config.config import TestData

#before tests
def login(self):
    self.loginPage = LoginPage(self.driver)
    self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
    yield
def logout(self):
    self.logout = Helpers(self.driver)



