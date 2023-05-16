from selene.support.shared import browser
from selene import have, be
import os


class RegistationPage():

    def open(self):
        browser.config.window_width = 1024
        browser.config.window_height = 768
        browser.config.base_url = 'https://demoqa.com'
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_second_name(self, second_name):
        browser.element('#lastName').type(second_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self):
        browser.element('#gender-radio-1').double_click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
    
    def fill_date_of_Birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{month}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}.react-datepicker__day').click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def choose_hobbies(self):
        browser.element('label[for="hobbies-checkbox-3"]').click()

    def upload_picture(self, picture):
        return browser.element('#uploadPicture').send_keys(os.getcwd() + f"\\{picture}")

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').set_value(state).press_tab()
        browser.element('#city').click()
        browser.element('#react-select-4-input').set_value(city).press_tab()

    def press_button_submit(self):
        browser.element('#submit').press_enter()

    def assert_student_data(
            self, student_name, student_email, student_gender, student_mobile, student_birthday,
            student_subjects, student_hobbies, student_picture, student_address, student_state_and_city):
        browser.all('tbody tr').should(have.exact_texts(student_name, student_email, student_gender,
                                                        student_mobile, student_birthday, student_subjects,
                                                        student_hobbies, student_picture,
                                                        student_address, student_state_and_city
                                                        ))
