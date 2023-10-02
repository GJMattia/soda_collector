from django.db import models

from django.urls import reverse

from datetime import date

TIMES = (
    ('AM', 'Before Noon'),
    ('PM', 'After Noon')
)


class Store(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores_detail', kwargs={'pk': self.id})


class Soda(models.Model):
    name = models.CharField(max_length=20)
    parent_company = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    release_year = models.IntegerField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'soda_id': self.id})

    def full_for_today(self):
        return self.consumption_set.filter(date=date.today()).count() >= len(TIMES)


class Consumption(models.Model):
    date = models.DateField('Consumption Date')
    time = models.CharField(
        max_length=2,
        choices=TIMES,
        default=TIMES[0][0]
    )

    soda = models.ForeignKey(Soda, on_delete=models.CASCADE)

    def __st__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
