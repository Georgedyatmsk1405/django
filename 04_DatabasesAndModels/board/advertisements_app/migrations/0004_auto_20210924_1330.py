# Generated by Django 2.2 on 2021-09-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_auto_20210924_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisementcontact',
            old_name='price',
            new_name='number',
        ),
    ]