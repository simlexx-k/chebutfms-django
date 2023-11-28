from django.core.management.base import BaseCommand
from faker import Faker
from fms.models import Farmer, Employee

fake = Faker()

class Command(BaseCommand):
    help = 'Populate farmers'

    def handle(self, *args, **kwargs):
        employees = Employee.objects.all()

        for employee in employees:
            phone_number = '07' + str(fake.random_number(digits=8))

            Farmer.objects.create(
                employee=employee,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=phone_number,
                address=fake.address(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated farmers'))
