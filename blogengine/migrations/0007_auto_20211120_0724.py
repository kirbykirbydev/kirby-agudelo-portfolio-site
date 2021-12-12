# Generated by Django 3.2.9 on 2021-11-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0006_alter_blogarticle_thumbnail_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='seo_url',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]