# Generated by Django 2.2.2 on 2019-07-23 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0016_guest_check_in_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='check_in_date',
        ),
    ]
