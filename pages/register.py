from base import BasePage
from locators import *
import utils


class RegisterPage(BasePage):

    def register(self, params, mismatch_password=False):
        self.find_element(*RegisterPageLocators.FIRSTNAME).send_keys(params.get('firstname', ''))
        self.find_element(*RegisterPageLocators.LASTNAME).send_keys(params.get('lastname', ''))
        self.find_element(*RegisterPageLocators.EMAIL).send_keys(params.get('email', ''))
        self.find_element(*RegisterPageLocators.PASSWORD).send_keys(params.get('password', ''))

        if mismatch_password != False:
            self.find_element(*RegisterPageLocators.CONFIRM_PASSWORD).send_keys(utils.random_string(8))
        else:
            self.find_element(*RegisterPageLocators.CONFIRM_PASSWORD).send_keys(params.get('password', ''))

        self.find_element(*RegisterPageLocators.PHONE).send_keys(params.get('phone', ''))
        self.find_element(*RegisterPageLocators.ZIP_CODE).send_keys(params.get('zipcode', ''))
        self.find_element(*RegisterPageLocators.CREATE_BUTTON).click()


    def _find_error_msg_element(self, msg_type):
        msgs = {
            'firstname': 'First Name Is Required',
            'lastname': 'Last Name Is Required',
            'email': 'Email Is Required',
            'password_match': 'Passwords Do Not Match.',
            'phone_number': 'Phone Number Is Required.',
            'zip': 'Zipcode Is Required.'
        }

        for p in self.find_elements(*RegisterPageLocators.PARAGRAPHS):
            print(p.text)
            if p.text == msgs[msg_type]:
                return p
        return None


    def is_first_name_error_displayed(self):
        if self._find_error_msg_element('firstname') is not None:
            return True


    def is_last_name_error_displayed(self):
        if self._find_error_msg_element('lastname') is not None:
            return True


    def is_email_error_displayed(self):
        if self._find_error_msg_element('email') is not None:
            return True


    def is_password_mismatch_error_displayed(self):
        if self._find_error_msg_element('password_match') is not None:
            return True


    def is_phone_error_displayed(self):
        if self._find_error_msg_element('phone_number') is not None:
            return True


    def is_zip_code_error_displayed(self):
        if self._find_error_msg_element('zip') is not None:
            return True


class ConfirmRegisterPage(BasePage):

    def is_service_available(self):
        try:
            self.find_element(*RegisterPageLocators.NOT_IN_AREA_TEXT).text
            return False
        except Exception as ex:
            return True


    def continue_registration(self):
        self.find_element(*RegisterPageLocators.REGISTER_DIFFERENT_AREA_BUTTON).click()
