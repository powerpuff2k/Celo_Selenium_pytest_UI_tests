from datetime import time
import pytest
from Tests.test_base import BaseTest
from Tests.test_base import loginTest
from Pages.PinSetupPage import PinSetUpPage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from pytest import fixture
class Test_PinSetup(BaseTest):

    def test_setUp_Pin(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        self.pinSetUp = PinSetUpPage(self.driver)
        self.pinSetUp.setup_pin(TestData.PIN)


