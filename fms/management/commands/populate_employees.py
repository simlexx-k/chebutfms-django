from django.core.management.base import BaseCommand
from faker import Faker
from fms.models import Employee

class Command(BaseCommand):
    help = 'Populate Employee model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Generate data for 100 employees (you can adjust the number)
            empid = fake.unique.random_int(min=1000, max=9999)
        

            Employee.objects.create(
                empid=empid,
               
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Employee model with fake data'))
