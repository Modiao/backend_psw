# Generated by Django 2.0 on 2020-06-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0002_auto_20200612_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='exo_file',
            field=models.FileField(upload_to=''),
        ),
    ]
