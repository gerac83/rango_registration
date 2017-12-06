import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango_reg.settings')

import django
django.setup()

from regapp.models import User, GitHub
from random import randint

def populate():
    for i in range(0,10):
        current_user = str(random_with_N_digits(7))+"a"
        user = User.objects.get_or_create(username=current_user, password="password",
                                          first_name=current_user, last_name=current_user, email=current_user+"@testuser.com")[0]
        user.set_password(user.password)
        user.save()
        page_url = "https://github.com/gerac83/rango_1.11.git"
        g = GitHub.objects.get_or_create(userid=current_user, url=page_url)[0]
        g.save()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Start execution here!
if __name__ == '__main__':
    print("Starting App population script...")
    populate()
