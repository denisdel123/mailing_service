from django.core.management import BaseCommand

from usersApp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        name_group = User.objects.get(pk=1)

        print(name_group.groups)