# Generated by Django 3.2.7 on 2021-10-08 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("plans", "0006_auto_20200504_1541"),
        ("ipn", "0008_auto_20181128_1032"),
    ]

    operations = [
        migrations.CreateModel(
            name="PayPalPayment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plans.order"
                    ),
                ),
                (
                    "paypal_ipn",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="ipn.paypalipn"
                    ),
                ),
                (
                    "user_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plans.userplan"
                    ),
                ),
            ],
        ),
    ]
