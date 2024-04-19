from django.core.management import BaseCommand

from mailingApp.models import Mailing
from usersApp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        ...



