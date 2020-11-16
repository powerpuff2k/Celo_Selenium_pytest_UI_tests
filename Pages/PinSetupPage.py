from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData



class PinSetUpPage(BasePage):
    PIN_NUMBER_FIELD = (By.ID, 'pin_code')
    PIN_CONFIRM_FIELD = (By.ID, "pin_code_confirm")
    NEXT_BUTTON = (By.XPATH, "//*[contains(@class, 'mat-button-wrapper') and text() = \" NEXT \"]")

    def __init__(self, driver):
        super().__init__(driver)

        """Page Actions"""

    def get_pinSetup_Page_title(self, title):
        return self.get_title(title)

    def pin_fields_visible(self):
        return self.is_visible(self.PIN_NUMBER_FIELD)

    def setup_pin(self, pin):
        self.do_send_keys(self.PIN_NUMBER_FIELD, pin)
        self.do_send_keys(self.PIN_CONFIRM_FIELD, pin)
        self.do_click(self.NEXT_BUTTON)





