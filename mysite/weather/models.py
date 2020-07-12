from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
