# Generated by Django 2.2 on 2021-12-03 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_files', '0002_auto_20211203_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='desctiption',
            new_name='description',
        ),
    ]
