# Generated by Django 2.0.7 on 2018-09-02 18:35

from django.db import migrations, models
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='articles_pictures/%Y/%m/%d/', verbose_name='Картинка статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='Список тэгов через запятую.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Заголовок'),
        ),
    ]
