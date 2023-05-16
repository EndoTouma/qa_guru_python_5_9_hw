from selene import have
from data.users import student
from model.registration_page import RegistrationPage


def test_filling_form(browser_go):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
    registration_page.close_modal()
