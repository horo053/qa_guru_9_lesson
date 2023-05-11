from demoqa_tests.registration_page import RegistrationPage
from demoqa_tests.users import student


def test_filling_form(browser_management):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.registration(student)

    registration_page.should_have_registered(student)