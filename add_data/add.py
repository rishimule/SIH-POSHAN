from schools.models import School, Class, Student
from districts.models import District
from django.contrib.auth.models import User
from faker import Faker
from faker_education import SchoolProvider
import random
from pathlib import Path
from django.core.files import File
from slugify import slugify


def add_school(num=1):
    fake = Faker('en_IN')
    fake.add_provider(SchoolProvider)
    path = Path('media/images/profile/state/default/default_state.png')
    for _ in range(num):
        print(f'Now Adding -------> {_}')
        name = fake.school_name()
        email = f"{slugify(name)}@gmail.com"
        user = User.objects.create_user(
            username=slugify(name),
            email=email,
            password='9223320271aA@'
        )
        user.save()
        udise_code = fake.bothify(text=f"############", letters='ABCDE')
        address_line1 = fake.street_address()
        address_line2 = fake.street_name()
        pincode = random.randint(400001, 420000)
        district = District.objects.order_by('?').first()
        contact_number = fake.bothify(text=f"9#########", letters='ABCDE')

        try:
            school = School(
                user=user,
                email=email,
                name=name,
                udise_code=udise_code,
                address_line1=address_line1,
                address_line2=address_line2,
                pincode=pincode,
                district=district,
                contact_number=contact_number
            )
            school.save()
            with path.open(mode='rb') as f:
                school.profile_pic = File(f, name=path.name)
                school.save()
            print(school)
            school.save()
            print('saved')
        except Exception as e:
            print(e)
            print('Not SAVED')


def add_class(num=1):
    fake = Faker('en_IN')
    for _ in range(num):
        print(f'Now Adding -------> {_}')
        class_std = random.randint(-2, 10)
        while class_std==0:
            class_std = random.randint(-2, 10)
        class_name = fake.bothify(text=f"{class_std}?", letters='ABCDE')
        year = random.randint(2022, 2023)
        school = School.objects.order_by('?').first()
        try:
            myclass = Class(
                class_std=class_std,
                class_name=class_name,
                year=year,
                school=school
            )
            print(myclass)
            myclass.save()
            print('saved')
        except Exception as e:
            print(e)
            print('Not SAVED')


def add_student(num=1):
    fake = Faker('en_IN')
    for _ in range(num):
        print(f'Now Adding -------> {_}')
        first_name = fake.first_name()
        last_name = fake.last_name()
        mother_name = fake.first_name_female()
        father_name = fake.first_name_male()
        dob = fake.date_between(
            start_date="-15y",
            end_date="-6y"
        )
        current_class = Class.objects.order_by('?').first()
        gr_no = fake.bothify(text=f"############", letters='ABCDE')
        gender = 'Male' if bool(random.getrandbits(1)) else 'Female'
        current_height = random.randint(8.0, 160)
        current_weight = random.randint(35, 60)

        try:
            student = Student(
                first_name=first_name,
                last_name=last_name,
                mother_name=mother_name,
                father_name=father_name,
                current_class=current_class,
                gr_no=gr_no,
                dob=dob,
                gender=gender,
                current_height=current_height,
                current_weight=current_weight,
            )
            print(student)
            student.save()
            print('saved')

        except Exception as e:
            print(e)
            print('Not SAVED')

