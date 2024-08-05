# Generated by Django 4.2.13 on 2024-07-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='request',
            name='vacancy',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
    ]
