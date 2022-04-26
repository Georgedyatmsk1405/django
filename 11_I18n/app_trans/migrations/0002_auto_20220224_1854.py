# Generated by Django 2.2 on 2022-02-24 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_trans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_trans_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
