# Generated by Django 4.1.7 on 2023-06-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("PG", "Pg"),
                            ("PG-13", "Pg 13"),
                            ("R", "R"),
                            ("NC-17", "Nc 17"),
                            ("G", "Default"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MovieOrder",
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
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movie_orders",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]
