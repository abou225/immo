# Generated by Django 4.2.14 on 2024-07-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
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
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("price", models.PositiveIntegerField()),
                ("superficy", models.PositiveIntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("villa", "Villa"),
                            ("appartement", "Appartement"),
                            ("store", "Store"),
                        ],
                        max_length=30,
                    ),
                ),
                ("address", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="properties/")),
                ("bedrooms", models.PositiveSmallIntegerField()),
                ("bathrooms", models.PositiveSmallIntegerField()),
            ],
        ),
    ]