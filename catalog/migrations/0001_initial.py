# Generated by Django 4.0.6 on 2022-07-27 13:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for item type', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter last name', max_length=20)),
                ('email', models.EmailField(help_text='Enter e-mail', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter phone number', max_length=128, region='BY')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a short name for item', max_length=200)),
                ('type', models.CharField(choices=[('l', 'Lost'), ('f', 'Found')], default='f', help_text='Choose item type', max_length=1)),
                ('description', models.TextField(blank=True, help_text='Enter description for item', max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='images/items')),
                ('city', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.contact')),
            ],
        ),
    ]
