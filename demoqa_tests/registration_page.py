from selene import browser, have
import os

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id=firstName]').type(value)

    def fill_last_name(self, value):
        browser.element('[id=lastName]').type(value)

    def fill_email(self, value):
        browser.element('[id=userEmail]').type(value)

    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()

    def fill_mobile_phone(self, value):
        browser.element('[id=userNumber]').set(value)

    def fill_date(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--00{day}:not(.react-datepicker__day--outside-mounth)').click()

    def fill_subjects(self, value):
        browser.element('[id=subjectsInput]').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, picture):
        browser.element('[id=uploadPicture]').send_keys(os.getcwd() + f'/{picture}')

    def fill_address(self, value):
        browser.element('[id=currentAddress]').type(value)

    def fill_state(self, value):
        browser.element('[id=react-select-3-input]').type(value).press_enter()

    def fill_city(self, value):
        browser.element('[id=react-select-4-input]').type(value).press_enter()

    def submit(self):
        browser.element('[id=submit]').press_enter()

    def should_have_registered(self, full_name, email, gender, number, birthday, subject,
                               hobby, picture, current_address, state_and_city):
        browser.all('tbody tr') .should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {email}',
            f'Gender {gender}',
            f'Mobile {number}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {hobby}',
            f'Picture {picture}',
            f'Address {current_address}',
            f'State and City {state_and_city}')
        )