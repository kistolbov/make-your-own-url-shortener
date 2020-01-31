from django.db import models


class URL(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    url = models.URLField(max_length=200)
    public_date = models.DateTimeField(auto_now=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.url