from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Item(models.Model):

    ITEM_TYPES = [('lost', 'Страчана'), ('found', 'Знойдзена')]

    name = models.CharField(blank=False, max_length=200)
    type = models.CharField(blank=False, max_length=5, choices=ITEM_TYPES)
    description = models.CharField(blank=True, max_length=1000)
    image = models.ImageField(blank=True, upload_to='uploads/img')
    first_name = models.CharField(blank=False, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=False)
    phone_number = PhoneNumberField(blank=False, region='BY')
    city = models.CharField(blank=False, max_length=20)
    address = models.CharField(blank=False, max_length=50)

    def __str__(self) -> str:
        return self.name