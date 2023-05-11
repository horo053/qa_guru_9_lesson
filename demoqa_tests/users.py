from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    arts = 'Arts'
    maths = 'Maths'
    biology = 'Biology'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    birthday: date
    subject: List[Subject]
    hobbies: List[Hobby]
    picture: str
    address: str
    state: str
    city: str


student = User(
    first_name='Ivan',
    last_name='Ivanovich',
    email='ivantest@mail.ru',
    gender=Gender.male,
    phone_number='8999777666',
    birthday=date(1995, 10, 9),
    subject=[Subject.arts],
    hobbies=[Hobby.music, Hobby.sports],
    picture='test.png',
    address='Moscow are',
    state='Uttar Pradesh',
    city='Lucknow')