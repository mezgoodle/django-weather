from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        """Need for the admin panel and more"""
        return self.name

    class Meta:
        """Configuration"""
        ordering = ['-id']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
