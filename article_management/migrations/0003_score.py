# Generated by Django 4.1 on 2023-11-26 12:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article_management", "0002_auto_20231126_1151"),
    ]

    operations = [
        migrations.CreateModel(
            name="Score",
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
                    "score",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1),
                            django.core.validators.MaxValueValidator(limit_value=5),
                        ]
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="article_management.article",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("article", "user")},},
        ),
    ]