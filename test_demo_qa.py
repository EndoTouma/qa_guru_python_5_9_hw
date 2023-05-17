from model.registration_page import RegistrationPage


def test_form(browser_go):
	registration_page = RegistrationPage()
	registration_page.open()
	
	registration_page.fill_first_name('Evgenii')
	registration_page.fill_second_name('Vervai')
	registration_page.fill_email('demo@test.ru')
	registration_page.choose_gender()
	registration_page.fill_phone_number('8800555353')
	registration_page.fill_date_of_Birth('26', '6', '1994')
	registration_page.fill_subjects('Computer Science')
	registration_page.choose_hobbies()
	registration_page.upload_picture('image.png')
	registration_page.fill_current_address('Russia, SP')
	registration_page.choose_state_and_city('Haryana', 'Panipat')
	registration_page.press_button_submit()
	registration_page.assert_student_data('Student Name Evgenii Vervai', 'Student Email demo@test.ru', 'Gender Male',
	                                     'Mobile 8800555353',
	                                     'Date of Birth 26 June,1994', 'Subjects Computer Science',
	                                     'Hobbies Music',
	                                     'Picture image.png', 'Address Russia, SP',
	                                     'State and City Haryana Panipat')
