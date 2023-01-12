# The simplest function to get the user email (copy to src/user_functions.py)
# def get_email_from_input():
#     """ Contains '@' and '.' """
#     return input("Tell me your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

# Tests (copy to tests/test_user_functions.py)
import pytest
import io
# from user_functions import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'
# Do the same for the following userName and password
#
# def get_user_name_from_input():
#     """ Not empty string. No spaces. """
#     user_name = input("Create your user name: ")
#
#     if ("@" not in email or "." not in email):
#         print('Name is not valid.')
#     else:
#         return user_name
#
# def get_password_from_input():
#     """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
#     user_password = input("Create your password: ")
#     if ("@" not in user_password or "." not in user_password):
#         print('Password is not valid.')
#     else:
#         return user_password