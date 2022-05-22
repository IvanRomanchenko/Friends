from django.core.management.base import BaseCommand

from account.orm import profile_count


class Command(BaseCommand):
    help = 'Prints all model instances count'

    def add_arguments(self, parser):
        parser.add_argument(
            '-w',
            '--with_staff',
            action='store_true',
            default=False,
            help='Counting with staff'
        )

    def handle(self, with_staff, **kwargs):
        count = profile_count(with_staff)

        if count == 1:
            self.stdout.write(f"{count} profile")
        else:
            self.stdout.write(f"{count} profiles")
