from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class SendMessage(BasePage):

    CHAT_LIST_ITEM = (By.CLASS_NAME, "conversation-card")
    MESSAGE_FROM_SENDER = (By.CLASS_NAME, "message-set from-sender")
    # TEXT_MESSAGE = (By.XPATH, "//*[contains(text(), \"__custom_name__\")]")
    TEXT_MESSAGE_FIELD = (By.ID, "celo-send-message-textarea")
    SEND_CHAT_BUTTON = (By.XPATH, "//*[contains(@class, 'notranslate') and text() = \"send\"]")
    MY_MESSAGE = (By.CLASS_NAME, "my-card")


    def __init__(self, driver):
        super().__init__(driver)

    """"Page actions"""
    def message_exists(self):
        return self.is_visible(self.CHAT_LIST_ITEM)

    def click_message(self):
        self.do_click(self.CHAT_LIST_ITEM)

    def view_message(self):
        return self.is_visible(self.MESSAGE_FROM_SENDER)

    def send_message(self, message):
        self.do_send_keys(self.TEXT_MESSAGE_FIELD, message)
        self.do_click(self.SEND_CHAT_BUTTON)

    def verify_message_sent(self):
        return self.is_visible(self.MY_MESSAGE)



