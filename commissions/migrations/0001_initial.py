# Generated by Django 5.1.6 on 2025-04-16 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commission",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Open", "Open"),
                            ("Full", "Full"),
                            ("Completed", "Completed"),
                            ("Discontinued", "Discontinued"),
                        ],
                        default="Open",
                        max_length=15,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commissions",
                        to="user_management.profile",
                    ),
                ),
            ],
            options={
                "ordering": ["created_on"],
            },
        ),
        migrations.CreateModel(
            name="Job",
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
                ("role", models.TextField(max_length=255)),
                ("manpower_required", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("Open", "Open"), ("Full", "Full")],
                        default="Open",
                        max_length=15,
                    ),
                ),
                (
                    "commission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="commissions.commission",
                    ),
                ),
            ],
            options={
                "ordering": ["status", "-manpower_required", "role"],
            },
        ),
        migrations.CreateModel(
            name="JobApplication",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Accepted", "Accepted"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=15,
                    ),
                ),
                ("applied_on", models.DateTimeField(auto_now_add=True)),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="user_management.profile",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="commissions.job",
                    ),
                ),
            ],
            options={
                "ordering": ["status", "-applied_on"],
            },
        ),
    ]
