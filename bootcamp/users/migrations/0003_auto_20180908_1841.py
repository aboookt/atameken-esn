# Generated by Django 2.0.7 on 2018-09-08 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180728_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='facebook_account',
        ),
        migrations.RemoveField(
            model_name='user',
            name='linkedin_account',
        ),
    ]
