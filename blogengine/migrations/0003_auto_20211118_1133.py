# Generated by Django 3.2.9 on 2021-11-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0002_alter_blogarticle_publish_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='preview',
            field=models.TextField(),
        ),
    ]
