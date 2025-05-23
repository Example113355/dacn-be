# Generated by Django 5.1.1 on 2025-05-14 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0004_remove_item_is_seed_item_category_item_plant_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="plant_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="plant_items",
                to="item.item",
            ),
        ),
    ]
