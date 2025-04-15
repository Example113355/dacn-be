from django.core.management.base import BaseCommand

from authentication.factories.user_factory import UserFactory


class Command(BaseCommand):
    help = "Seed the database with Customer data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, help="The number of customers to create", default=10
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        self.stdout.write(f"Seeding {count} customers...")
        for _ in range(count):
            UserFactory()
        self.stdout.write(f"{count} customers created successfully!")
