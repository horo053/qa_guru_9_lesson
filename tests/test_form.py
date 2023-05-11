from demoqa_tests.registration_page import RegistrationPage


def test_form(browser_management):
    #открытие браузера
    registration_page = RegistrationPage()
    registration_page.open()

    #заполнение полей: Name, Email, Gender, Mobile
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanovich')
    registration_page.fill_email('ivantest@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile_phone('8999777666')

    #Выбор даты рождения - Date of Birth
    registration_page.fill_date('9', 'October', '1995')

    #заполнение полей: Subjects, Hobbies
    registration_page.fill_subjects('Arts')
    registration_page.fill_hobbies('Music')

    #загрузка файла - Picture
    registration_page.upload_picture('test.png')

    #заполнение полей: Current Address, State and City
    registration_page.fill_address('Moscow')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')

    #нажатие на кнопку - Submit
    registration_page.submit()

    #проверка результирующей таблицы
    registration_page.should_have_registered(
        'Ivan Ivanovich',
        'ivantest@mail.ru',
        'Male',
        '8999777666',
        '09 October,1995',
        'Arts',
        'Music',
        'test.png',
        'Moscow',
        'Haryana Panipat'
    )