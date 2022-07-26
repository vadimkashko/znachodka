from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Item(models.Model):

    ITEM_TYPES = [('l', 'Lost'), ('f', 'Found')]

    name = models.CharField(blank=False, max_length=200)
    type = models.CharField(blank=False, max_length=1, choices=ITEM_TYPES)
    description = models.CharField(blank=True, max_length=1000)
    image = models.ImageField(blank=True, upload_to='images/items')
    first_name = models.CharField(blank=False, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=False)
    phone_number = PhoneNumberField(blank=False, region='BY')
    city = models.CharField(blank=False, max_length=20)
    address = models.CharField(blank=False, max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.name
