import factory
from faker import Faker

from authentication.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    full_name = factory.Faker("name")
    email = factory.LazyAttribute(lambda _: fake.unique.email())
    password = factory.Faker("password")
