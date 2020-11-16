import time
import pytest
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.Helpers import Helpers
from Pages.SendMessage import SendMessage
from Pages.PinSetupPage import PinSetUpPage
from Tests.test_base import BaseTest

class Test_Send_Message(BaseTest):

    @pytest.fixture(scope='class')
    def setup_module(self):
        self.login = LoginPage(self.driver)
        self.login.do_login(TestData.EMAIL, TestData.PASSWORD)
        self.pinSetUp = PinSetUpPage(self.driver)
        self.pinSetUp.setup_pin(TestData.PIN)
        yield
        self.logout = Helpers(self.driver)
        self.logout.logout()

    def test_message_is_available(self, setup_module):
        self.viewMessage = SendMessage(self.driver)
        flag = self.viewMessage.message_exists()
        assert flag

    def test_send_message(self, setup_module):
        self.viewMessage = SendMessage(self.driver)
        self.viewMessage.click_message()
        self.viewMessage.send_message(TestData.MESSAGE)
        sent_message = self.viewMessage.verify_message_sent()
        print("Result is", sent_message)



