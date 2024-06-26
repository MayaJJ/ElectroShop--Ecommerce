# Generated by Django 4.2.9 on 2024-01-12 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp1", "0014_alter_order_order_date_alter_reviews_review_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateField(
                blank=True, default=datetime.datetime(2024, 1, 12, 22, 23, 19, 161371)
            ),
        ),
        migrations.AlterField(
            model_name="reviews",
            name="review_time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2024, 1, 12, 22, 23, 19, 161371)
            ),
        ),
    ]
