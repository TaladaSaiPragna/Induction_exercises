from django.core.management.base import BaseCommand
from django.utils import timezone
from library import settings


class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Indicates name to display')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        time = timezone.now().strftime('%X')
        self.stdout.write("Hello %s !!! It's now %s" % (name, time))
