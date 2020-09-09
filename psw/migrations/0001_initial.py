# Generated by Django 2.1 on 2020-09-09 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('exercice_file', models.ImageField(blank=True, null=True, upload_to='media')),
                ('niveau', models.CharField(choices=[('1', 'Sixieme College'), ('2', 'Cinquieme College'), ('4', 'Quatrieme College'), ('5', 'troisieme College'), ('6', 'Seconde Lycee'), ('7', 'Premiere Lycee'), ('0', 'Terminale Lycee')], default=0, max_length=6)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalExercice',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('exercice_file', models.TextField(blank=True, max_length=100, null=True)),
                ('niveau', models.CharField(choices=[('1', 'Sixieme College'), ('2', 'Cinquieme College'), ('4', 'Quatrieme College'), ('5', 'troisieme College'), ('6', 'Seconde Lycee'), ('7', 'Premiere Lycee'), ('0', 'Terminale Lycee')], default=0, max_length=6)),
                ('description', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical exercice',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]