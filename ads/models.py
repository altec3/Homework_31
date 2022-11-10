from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, help_text="Краткое описание. Максимум 1000 символов")
    address = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
