from django.core.management.base import BaseCommand
from HomemWork2app.models import Client

class Command(BaseCommand):
    help = 'Get all users.'

    def handle(self, *args, **options):
        user = Client.objects.all()
        self.stdout.write(f'{user}')