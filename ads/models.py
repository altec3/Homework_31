from django.db import models


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, help_text="Краткое описание. Максимум 1000 символов")
    address = models.CharField(max_length=500)
    is_published = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
