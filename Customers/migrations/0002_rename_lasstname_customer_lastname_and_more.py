# Generated by Django 4.2.14 on 2024-07-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customers", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="lasstname",
            new_name="lastname",
        ),
        migrations.AlterField(
            model_name="customer",
            name="birthday",
            field=models.DateField(),
        ),
    ]
