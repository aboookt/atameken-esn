# Generated by Django 2.0.7 on 2018-08-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0013_auto_20180829_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(blank=True, default='', upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
    ]
