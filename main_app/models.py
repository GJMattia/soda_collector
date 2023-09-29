from django.db import models

from django.urls import reverse


class Soda(models.Model):
    name = models.CharField(max_length=20)
    parent_company = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'soda_id': self.id})
