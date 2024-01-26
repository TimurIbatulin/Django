from django.core.management.base import BaseCommand
from HomemWork2app.models import Client


class Command(BaseCommand):
    help = 'Get user by id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')