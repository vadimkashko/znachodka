from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(blank=False,
                            max_length=100,
                            unique=True,
                            help_text='Category name',
                            db_index=True)

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
                                  help_text='First name')
    last_name = models.CharField(blank=False,
                                 max_length=20,
                                 help_text='Last name')
    email = models.EmailField(blank=False,
                              help_text='E-mail',
                              unique=True)
    phone_number = PhoneNumberField(blank=False,
                                    help_text='Phone number',
                                    unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return ' '.join((self.first_name, self.last_name))


class Item(models.Model):

    LOST = 'l'
    FOUND = 'f'
    ITEM_TYPES = [(LOST, 'lost'), (FOUND, 'found')]

    is_active = models.BooleanField(blank=False,
                                    default=True,
                                    editable=False,
                                    help_text='Item status')
    name = models.CharField(blank=False,
                            max_length=200,
                            help_text='Short name for item')
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 blank=False,
                                 null=True,
                                 help_text='Item category')
    type = models.CharField(blank=False,
                            max_length=1,
                            choices=ITEM_TYPES,
                            default=FOUND,
                            help_text='Item type')
    city = models.CharField(blank=False, max_length=20)
    description = models.TextField(blank=True,
                                   max_length=1000,
                                   help_text='Description for item')
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    who_found = models.ForeignKey(Contact,
                                  on_delete=models.DO_NOTHING,
                                  blank=True,
                                  related_name='who_found',
                                  null=True)
    who_lost = models.ForeignKey(Contact,
                                 on_delete=models.DO_NOTHING,
                                 blank=True,
                                 related_name='who_lost',
                                 null=True)
    image = models.ImageField(blank=True,
                              upload_to='images/items',
                              default='images/items/default_item.png',
                              help_text='Photo of item')

    def __str__(self) -> str:
        return self.name

    def get_type(self) -> str:
        for pair in self.ITEM_TYPES:
            if self.type in pair:
                return pair[1]

    def get_status(self) -> str:
        if self.is_active:
            return 'opened'
        return 'closed'
