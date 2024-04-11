from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Название", max_length=200, db_index=True)
    slug = models.SlugField("Slug", max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50)
    slug = models.SlugField("Slug", max_length=200, db_index=True)
    cover = models.ImageField("Фото", upload_to="images/", blank=True)
    description = models.CharField("Краткое описание", max_length=250)
    full_text = models.TextField("Основная информация")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Количество")
    available = models.BooleanField("Наличие", default=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug'),)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])