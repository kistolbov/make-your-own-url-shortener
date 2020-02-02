from django.db import models


class URL(models.Model):
    url = models.URLField(max_length=1000)
    short_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.url