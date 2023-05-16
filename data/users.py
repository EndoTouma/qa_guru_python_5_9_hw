import dataclasses
from typing import List
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birthday: date
    subjects: str
    hobby: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


student = User(
	first_name='Evgenii',
	last_name='Vervaii',
	email='demo@test.ru',
	gender='Male',
	mobile='8800555353',
	birthday=date(1994, 6, 26),
	subjects='Computer Science',
	hobby='3',
	hobbies='Music',
	picture='image.png',
	address='Russia, SP',
	state='Haryana',
	city='Panipat'
)
