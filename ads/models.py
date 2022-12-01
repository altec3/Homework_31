from django.db import models

from categories.models import Category
from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(
        max_length=1000,
        help_text="Краткое описание. Максимум 1000 символов",
        blank=True,
        null=True
    )
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
