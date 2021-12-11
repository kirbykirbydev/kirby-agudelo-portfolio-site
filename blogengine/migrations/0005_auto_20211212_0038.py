# Generated by Django 3.2.9 on 2021-12-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0004_rename_tag_blogarticle_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtag',
            name='url_slug',
            field=models.SlugField(default='test', max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
