import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_first=fakegen.first_name()
        fake_last=fakegen.last_name()
        fake_email=fakegen.email()

        user=User.objects.get_or_create(FirstName=fake_first,LastName=fake_last,Email=fake_email)[0]

if __name__=='__main__':
    print("populating start!")
    populate(20)
    print("populating end!")
