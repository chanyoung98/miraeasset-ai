# Generated by Django 5.0.2 on 2024-07-25 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("matching", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="easy_summary",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="matching.crawling"
            ),
        ),
    ]
