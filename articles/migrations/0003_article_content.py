# Generated by Django 2.2.6 on 2019-10-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
