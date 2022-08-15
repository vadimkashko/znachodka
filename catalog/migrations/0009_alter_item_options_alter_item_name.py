# Generated by Django 4.0.6 on 2022-08-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_category_options_alter_city_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-create_date']},
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Short name for item', max_length=20),
        ),
    ]
