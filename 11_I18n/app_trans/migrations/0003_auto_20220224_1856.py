# Generated by Django 2.2 on 2022-02-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_trans', '0002_auto_20220224_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='like',
            field=models.IntegerField(default=0, null=True),
        ),
    ]