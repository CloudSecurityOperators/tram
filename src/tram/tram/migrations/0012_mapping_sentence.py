# Generated by Django 3.1.6 on 2021-03-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0011_auto_20210305_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapping',
            name='sentence',
            field=models.TextField(default='test sentence'),
            preserve_default=False,
        ),
    ]