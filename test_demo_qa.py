from model.registration_page import RegistationPage


def test_form():
	registation_page = RegistationPage()
	
	registation_page.open()
	registation_page.fill_first_name('Evgenii')
	registation_page.fill_second_name('Vervai')
	registation_page.fill_email('demo@test.ru')
	registation_page.choose_gender()
	registation_page.fill_phone_number('8800555353')
	registation_page.fill_date_of_Birth('26', '6', '1994')
	registation_page.fill_subjects('Computer Science')
	registation_page.choose_hobbies()
	registation_page.upload_picture('image.png')
	registation_page.fill_current_address('Russia, SP')
	registation_page.choose_state_and_city('Haryana', 'Panipat')
	registation_page.press_button_submit()
	registation_page.assert_student_data('Student Name Evgenii Vervai', 'Student Email demo@test.ru', 'Gender Male',
	                                     'Mobile 8800555353',
	                                     'Date of Birth 26 June,1994', 'Subjects Computer Science',
	                                     'Hobbies Music',
	                                     'Picture image.png', 'Address Russia, SP',
	                                     'State and City Haryana Panipat')
	registation_page.final_print()
