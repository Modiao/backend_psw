# Generated by Django 2.1 on 2020-09-10 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0003_auto_20200910_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corrections',
            old_name='course_file',
            new_name='correction_file',
        ),
        migrations.RenameField(
            model_name='historicalcorrections',
            old_name='course_file',
            new_name='correction_file',
        ),
    ]
