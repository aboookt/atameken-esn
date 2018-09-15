# Generated by Django 2.0.7 on 2018-09-08 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180908_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+799999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=280, null=True, verbose_name='О компании'),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_type',
            field=models.CharField(choices=[('0111', 'Выращивание зерновых культур (за исключением риса), бобовых культур и масличных семян'), ('0112', 'Выращивание риса'), ('0113', 'Выращивание овощей и бахчевых, корнеплодов и клубнеплодов'), ('0114', 'Выращивание сахарного тростника'), ('0115', 'Выращивание табака'), ('0116', 'Выращивание волокнистых прядильных культур'), ('0119', 'Выращивание прочих сезонных культур'), ('0121', 'Выращивание винограда'), ('0122', 'Выращивание тропических и субтропических фруктов'), ('0123', 'Выращивание цитрусовых фруктов'), ('0124', 'Выращивание семечковых и косточковых плодов'), ('0125', 'Выращивание прочих видов плодовых деревьев, кустарников и орехов'), ('0126', 'Выращивание маслосодержащих плодов')], default='A', max_length=6, verbose_name='Вид деятельности'),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=50, null=True, verbose_name='Название предприятия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('akmola', 'Акмолинская область'), ('aktobe', 'Актюбинская область'), ('almaty', 'Алматинская область'), ('atyrau', 'Атырауская область'), ('eastern', 'Восточно-Казахстанская область'), ('dzhambul', 'Жамбылская область'), ('western', 'Западно-Казахстанская область'), ('karaganda', 'Карагандинская область'), ('kostanai', 'Костанайская область'), ('kyzylorda', 'Кызылординская область'), ('mangystau', 'Мангистауская область'), ('pavlodar', 'Павлодарская область'), ('north', 'Северо-Казахстанская область'), ('turkestan', 'Туркестанская область')], default='akmola', max_length=6, verbose_name='Область'),
        ),
    ]
