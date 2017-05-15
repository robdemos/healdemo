import random, string
from random import randint
import phonenumbers # thanks google and daviddrysdale


def random_password(length):
    '''Generates random password'''
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def random_string(length):
    '''Generates a random string'''
    return ''.join(random.choice(string.lowercase) for _ in range(length))


def random_email(domain='mailinator.com'):
    '''generates a random email address'''
    return '{}@{}'.format(random_string(6), domain)


def random_usa_phone():
    '''generates a random valid us phone number'''
    base_num = phonenumbers.parse(str('+1' + str(randint(2130000000, 9999999999))), None)
    while phonenumbers.is_valid_number(base_num) is False:
        base_num = phonenumbers.parse(str('+1' + str(randint(2130000000, 9999999999))), None)
    return str(base_num.national_number)


def random_zip():
    return str(randint(10000, 99999))