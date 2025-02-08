from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self) -> str:
        return self.title
