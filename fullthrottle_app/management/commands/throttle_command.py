from django.core.management.base import BaseCommand
from django.utils import timezone
from fullthrottle_app.models import ActivityPeriod,User
from datetime import datetime 
import random
from random import randint,randrange
from datetime import datetime,timedelta
from faker import Faker

# function to generate random date and time
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Custom command to bulk upload User data
class Command(BaseCommand):
    help = 'Bulk upload Dummy data to user and ActivityPeriod Model'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Enter the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        username = []
        for _ in range(total):
            faker = Faker()
            username.append(faker.name())
        tz = ['America/Los_Angeles','Asia/Kolkata']
        start_time = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
        end_time = datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
        for name in username:
            random_start_time = random_date(start_time, end_time)
            random_end_time = random_date(start_time, end_time)
            user_instance = User.objects.create_user(
                    username=name,
                    password=name,
                    tz=random.choice(tz),
                    first_name=name
                )
            for i in range(3):
                activity_instance = ActivityPeriod.objects.create(
                        user=user_instance,
                        start_time=random_start_time,
                        end_time=random_end_time
                    )
        self.stdout.write(self.style.SUCCESS("Bulk data uploaded Successfully"))