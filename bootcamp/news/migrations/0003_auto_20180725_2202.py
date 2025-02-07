# Generated by Django 2.0.7 on 2018-07-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_four',
            field=models.TextField(default='content_four', max_length=1000),
        ),
        migrations.AddField(
            model_name='news',
            name='content_three',
            field=models.TextField(default='content_three', max_length=1000),
        ),
        migrations.AddField(
            model_name='news',
            name='content_two',
            field=models.TextField(default='content_two', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
