# Generated by Django 5.1.6 on 2025-04-17 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "description",
                    models.TextField(default="A buyable item of this merch store."),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=24)),
                ("stock", models.PositiveIntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("On Sale", "On Sale"),
                            ("Out of Stock", "Out Of Stock"),
                        ],
                        default="Out of Stock",
                        max_length=12,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="user_management.profile",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="merchstore.producttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("On Cart", "On Cart"),
                            ("To Pay", "To Pay"),
                            ("To Ship", "To Ship"),
                            ("To Receive", "To Receive"),
                            ("Delivered", "Delivered"),
                        ],
                        default="On Cart",
                        max_length=12,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="transaction",
                        to="user_management.profile",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="transaction",
                        to="merchstore.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
                "ordering": ["buyer"],
            },
        ),
    ]
