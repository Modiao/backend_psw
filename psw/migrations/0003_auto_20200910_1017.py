# Generated by Django 2.1 on 2020-09-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0002_auto_20200910_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='corrections',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='historicalcorrections',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='historicalcourses',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='historicalexercices',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]