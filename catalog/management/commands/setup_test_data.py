import random
from time import sleep

from django.db import transaction
from django.core.management.base import BaseCommand

from catalog.models import Category, Contact, Item
from catalog.factories import (CategoryFactory, ContactFactory, ItemFactory)

NUM_CONTACTS = 50
NUM_CATEGORIES = 10
NUM_ITEMS = 500


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Contact, Category, Item]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the contacts
        contacts = []
        for _ in range(NUM_CONTACTS):
            category = ContactFactory()
            contacts.append(category)

        # Create all the categories
        categories = []
        for _ in range(NUM_CATEGORIES):
            category = CategoryFactory()
            categories.append(category)

        # Create all the items
        for _ in range(NUM_ITEMS):
            sleep(0.01)
            contact = random.choice(contacts)
            category = random.choice(categories)
            ItemFactory(contact=contact, category=category)

        self.stdout.write("Test data was generated!")