# Generated by Django 3.1.7 on 2021-04-11 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0004_auto_20210411_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 11, 16, 47, 42, 220180)),
        ),
    ]
