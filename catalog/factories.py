import factory
from factory.django import DjangoModelFactory, ImageField

from catalog.models import Category, Contact, Item


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = factory.Faker('word')


class ContactFactory(DjangoModelFactory):

    class Meta:
        model = Contact
        django_get_or_create = ('email', 'phone_number',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('msisdn')


class ItemFactory(DjangoModelFactory):

    class Meta:
        model = Item
        django_get_or_create = ('category', 'contact',)

    name = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)
    type = factory.Faker('random_element', elements=('l', 'f'))
    description = factory.Faker("paragraph",
                                nb_sentences=5,
                                variable_nb_sentences=True)
    city = factory.Faker('city')
    contact = factory.SubFactory(ContactFactory)
    image = ImageField()
    # image = factory.Faker('image', size=(1280, 1024))
