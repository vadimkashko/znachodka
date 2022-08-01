# Generated by Django 4.0.6 on 2022-07-31 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_item_category_alter_item_who_found_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='who_found',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='who_found', to='catalog.contact'),
        ),
        migrations.AlterField(
            model_name='item',
            name='who_lost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='who_lost', to='catalog.contact'),
        ),
    ]
