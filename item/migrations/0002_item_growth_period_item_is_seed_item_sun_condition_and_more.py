# Generated by Django 5.1.1 on 2025-05-01 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="growth_period",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="is_seed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="sun_condition",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="water_condition",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="SeedItem",
        ),
    ]
