# Generated by Django 2.2.2 on 2019-07-21 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='Room_code',
            new_name='Roomcode',
        ),
        migrations.RenameField(
            model_name='rooms',
            old_name='Room_type_code',
            new_name='Roomtypecode',
        ),
        migrations.RenameField(
            model_name='rooms',
            old_name='type_name',
            new_name='typename',
        ),
    ]
