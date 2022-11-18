from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(decimal_places=6, max_digits=8, null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=8, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name
