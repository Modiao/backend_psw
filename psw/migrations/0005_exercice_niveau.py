# Generated by Django 3.1 on 2020-08-13 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0004_auto_20200813_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='niveau',
            field=models.CharField(choices=[('6ieme', 'sixieme college'), ('5ieme', 'cinquieme college')], default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
    ]