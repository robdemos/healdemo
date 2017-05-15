from selenium.webdriver.common.by import By


class RegisterPageLocators(object):
    # Should work on a better solution than using these xpaths
    FIRSTNAME = (By.NAME, 'firstname')
    LASTNAME = (By.NAME, 'lastname')
    EMAIL = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    CONFIRM_PASSWORD = (By.NAME, 'password2')
    PHONE = (By.NAME, 'phonenumber')
    COUNTRY_SELECTOR = (By.CLASS_NAME, 'selected-flag')
    ZIP_CODE = (By.NAME, 'zipcode')
    CREATE_BUTTON = (By.XPATH, '//*[@id="register-view"]/form/div[9]/button')
    LOGIN_LINK = (By.LINK_TEXT, ' Log in')

    PARAGRAPHS = (By.TAG_NAME, 'p')

    CONTINUE_BUTTON = (By.XPATH, '//*[@id="register-view"]/div[2]/div[2]/button')
    NOT_IN_AREA_TEXT = (By.XPATH, '//*[@id="register-view"]/div[2]/h3')
    REGISTER_DIFFERENT_AREA_BUTTON = (By.XPATH, '//*[@id="register-view"]/div[2]/div[6]/button')
