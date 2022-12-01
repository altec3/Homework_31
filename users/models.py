from django.contrib.auth.models import AbstractUser
from django.db import models

from locations.models import Location


class User(AbstractUser):
    ADMIN = "admin"
    MEMBER = "member"
    MODERATOR = "moderator"

    ROLE = [
        (ADMIN, "Администратор"),
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор")
    ]
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveSmallIntegerField(null=True)
    location_id = models.ManyToManyField(Location)
    birth_date = models.DateField(default="1900-01-01")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username

    @property
    def total_ads(self):
        return self.ad_set.filter(is_published=True).count()
