# Generated by Django 2.2 on 2021-09-22 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]