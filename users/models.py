from django.db import models

from locations.models import Location


class User(models.Model):
    ROLE = [
        ("admin", "Администратор"),
        ("member", "Пользователь"),
        ("moderator", "Модератор")
    ]
    first_name = models.CharField(max_length=20, help_text="Имя. Максимум 20 символов", null=True)
    last_name = models.CharField(max_length=50, help_text="Фамилия. Максимум 50 символов", null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveIntegerField(null=True)
    location_id = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
