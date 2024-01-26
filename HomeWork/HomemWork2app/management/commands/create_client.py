from django.core.management.base import BaseCommand
from HomemWork2app.models import Client

class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        user = Client(name='John', email='j@yandex.ru', telefon_number='80000000000', adress='dcecfv', Clientregistration_date='2008-02-25')

        user.save()
        self.stdout.write((f'{user}'))