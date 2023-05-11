from selene import browser, have
import os


def test_form():
    #открытие браузера
    browser.open('/automation-practice-form')

    #заполнение полей: Name, Email, Gender, Mobile
    browser.element('[id=firstName]').type('Ivan')
    browser.element('[id=lastName]').type('Ivanovich')
    browser.element('[id=userEmail]').type('ivantest@mail.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('[id=userNumber]').set('8999777666')

    #Выбор даты рождения - Date of Birth
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value = "9"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value = "1995"]').click()
    browser.element('.react-datepicker__day--013').click()

    #заполнение полей: Subjects, Hobbies
    browser.element('[id=subjectsInput]').type('Arts').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()

    #загрузка файла - Picture
    #ответ найден на https://software-testing.ru/forum/index.php?/topic/33954-selenium-zagruzka-fajla-cherez-knopku-zagruzi/
    browser.element('[id=uploadPicture]').send_keys(os.getcwd() + '/test.png')

    #заполнение полей: Current Address, State and City
    browser.element('[id=currentAddress]').type('Moscow')
    browser.element('[id=react-select-3-input]').type('Haryana').press_enter()
    browser.element('[id=react-select-4-input]').type('Panipat').press_enter()

    #нажатие на кнопку - Submit
    browser.element('[id=submit]').press_enter()

    #проверка результирующей таблицы
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Ivan Ivanovich', 'Student Email ivantest@mail.ru', 'Gender Male', 'Mobile 8999777666',
        'Date of Birth 13 October,1995', 'Subjects Arts', 'Hobbies Music',
        'Picture test.png', 'Address Moscow', 'State and City Haryana Panipat'))