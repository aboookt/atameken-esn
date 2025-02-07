# Generated by Django 2.0.7 on 2018-08-09 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='verb',
            field=models.CharField(choices=[('L', 'liked'), ('D', 'disliked'), ('C', 'commented'), ('F', 'cavorited'), ('A', 'answered'), ('W', 'accepted'), ('E', 'edited'), ('K', 'also commented'), ('I', 'logged in'), ('O', 'logged out'), ('V', 'voted on'), ('S', 'shared'), ('U', 'created an account'), ('R', 'replied to')], max_length=1),
        ),
    ]
