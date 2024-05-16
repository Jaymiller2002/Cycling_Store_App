# Generated by Django 4.2.13 on 2024-05-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0004_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="color",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="number_in_stock",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="type",
            field=models.CharField(
                choices=[
                    ("unicycle", "Unicycle"),
                    ("bicycle", "Bicycle"),
                    ("tricycle", "Tricycle"),
                ],
                max_length=100,
            ),
        ),
    ]