from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(blank=False,
                            max_length=100,
                            unique=True,
                            help_text='Enter a name for item type')

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        """String for representing the Model object (in Admin site etc.)

        Returns:
            str: name
        """
        return self.name


class Contact(models.Model):
    first_name = models.CharField(blank=False,
                                  max_length=20,
                                  help_text='Enter name')
    last_name = models.CharField(blank=False,
                                 max_length=20,
                                 help_text='Enter last name')
    email = models.EmailField(blank=False,
                              help_text='Enter e-mail',
                              unique=True)
    phone_number = PhoneNumberField(blank=False,
                                    help_text='Enter phone number',
                                    unique=True)

    def __str__(self) -> str:
        return ' '.join((self.first_name, self.last_name))


class Item(models.Model):

    LOST = 'l'
    FOUND = 'f'
    ITEM_TYPES = [(LOST, 'Lost'), (FOUND, 'Found')]

    name = models.CharField(blank=False,
                            max_length=200,
                            help_text='Enter a short name for item')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=False,
                                 null=True)
    type = models.CharField(blank=False,
                            max_length=1,
                            choices=ITEM_TYPES,
                            default=FOUND,
                            help_text='Choose item type')
    description = models.TextField(blank=True,
                                   max_length=1000,
                                   help_text='Enter description for item')
    image = models.ImageField(blank=True, upload_to='images/items')
    city = models.CharField(blank=False, max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False)

    def __str__(self) -> str:
        return self.name
