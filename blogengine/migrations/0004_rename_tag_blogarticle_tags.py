# Generated by Django 3.2.9 on 2021-12-11 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0003_auto_20211211_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogarticle',
            old_name='tag',
            new_name='tags',
        ),
    ]
