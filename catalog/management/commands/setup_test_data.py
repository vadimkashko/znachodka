import random

from django.db import transaction
from django.core.management.base import BaseCommand

from catalog.models import Category, Contact, Item
from .factories import (CategoryFactory, ContactFactory, ItemFactory)

NUM_CONTACTS = 80
NUM_CATEGORIES = 10
NUM_ITEMS = 200


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
            contact = ContactFactory()
            contacts.append(contact)

        # Create all the categories
        categories = []
        for _ in range(NUM_CATEGORIES):
            category = CategoryFactory()
            categories.append(category)

        # Create all the items
        for _ in range(NUM_ITEMS):
            type = random.choice(['l', 'f'])
            contact = random.choice(contacts)
            category = random.choice(categories)
            if type == 'f':
                ItemFactory(type=type,
                            who_found=contact,
                            who_lost=None,
                            category=category)
            else:
                ItemFactory(type=type,
                            who_found=None,
                            who_lost=contact,
                            category=category)

        self.stdout.write("Test data was generated!")
