# Generated by Django 3.1.3 on 2021-01-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0004_auto_20201220_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
