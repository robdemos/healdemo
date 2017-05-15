import unittest
import driver_factory
from pages import register
from pages import utils
import pytest


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.driver = driver_factory.get_driver()
        self.driver.get('http://patient.heal.com/register')


    def tearDown(self):
        self.driver.quit()


    @pytest.mark.webtest
    def test_register_correct(self):
        params = {
            'firstname': utils.random_string(5),
            'lastname': utils.random_string(5),
            'email': utils.random_email(),
            'password': utils.random_string(8),
            'phone': utils.random_usa_phone(),
            'zipcode': utils.random_zip()
        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        confirm_reg_page = register.ConfirmRegisterPage(self.driver)
        assert confirm_reg_page.is_service_available() is False


    @pytest.mark.webtest
    def test_missing_firstname(self):
        params = {
            'lastname': utils.random_string(5),
            'email': utils.random_email(),
            'password': utils.random_string(8),
            'phone': utils.random_usa_phone(),
            'zipcode': utils.random_zip()
        }
        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        assert register_page.is_first_name_error_displayed() is True


    @pytest.mark.webtest
    def test_missing_lastname(self):
        params = {
        'firstname': utils.random_string(5),
        'email': utils.random_email(),
        'password': utils.random_string(8),
        'phone': utils.random_usa_phone(),
        'zipcode': utils.random_zip()

        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        assert register_page.is_last_name_error_displayed() is True


    @pytest.mark.webtest
    def test_missing_email(self):
        params = {
            'firstname': utils.random_string(5),
            'lastname': utils.random_string(5),
            'password': utils.random_string(8),
            'phone': utils.random_usa_phone(),
            'zipcode': utils.random_zip()
        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        assert register_page.is_email_error_displayed() is True


    @pytest.mark.webtest
    def test_missing_phone(self):
        #CAN REGISTER WITHOUT PHONE IF CLICKING THE PHONE INPUT, THEN INPUT ZIP AND CONTINUE REGISTERING
        params = {
            'firstname': utils.random_string(5),
            'lastname': utils.random_string(5),
            'email': utils.random_email(),
            'password': utils.random_string(8),
            'zipcode': utils.random_zip()
        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        assert register_page.is_phone_error_displayed() is True


    @pytest.mark.webtest
    def test_mismatched_password(self):
        params = {
            'firstname': utils.random_string(5),
            'lastname': utils.random_string(5),
            'email': utils.random_email(),
            'password': utils.random_string(8),
            'phone': utils.random_usa_phone(),
            'zipcode': utils.random_zip()
        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params, mismatch_password=True)

        assert register_page.is_password_mismatch_error_displayed() is True


    @pytest.mark.webtest
    def test_missing_zipcode(self):
        params = {
            'firstname': utils.random_string(5),
            'lastname': utils.random_string(5),
            'email': utils.random_email(),
            'password': utils.random_string(8),
            'phone': utils.random_usa_phone(),
        }

        register_page = register.RegisterPage(self.driver)
        register_page.register(params)

        assert register_page.is_zip_code_error_displayed() is True
