# Generated by Django 3.1.7 on 2021-04-18 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0009_auto_20210417_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 18, 11, 29, 44, 355602)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 18, 11, 29, 44, 356601)),
        ),
    ]
