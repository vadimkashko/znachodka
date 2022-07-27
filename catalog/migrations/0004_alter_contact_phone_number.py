# Generated by Django 4.0.6 on 2022-07-27 19:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_contact_email_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Enter phone number', max_length=128, region=None, unique=True),
        ),
    ]
