# Generated by Django 5.0.2 on 2024-04-07 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=200, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("name",),
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                ("slug", models.SlugField(max_length=200, verbose_name="Slug")),
                (
                    "cover",
                    models.ImageField(
                        blank=True, upload_to="images/", verbose_name="Фото"
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="Краткое описание"),
                ),
                ("full_text", models.TextField(verbose_name="Основная информация")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                ("stock", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Наличие"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="main.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ("name",),
            },
        ),
    ]
