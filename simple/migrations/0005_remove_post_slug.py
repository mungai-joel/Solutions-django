# Generated by Django 3.1.7 on 2021-07-28 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0004_auto_20210726_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
