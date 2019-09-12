from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    COUNTRY = (
        ('RU', 'Russia'),
        ('UKR', 'Ukraine'),
        ('US', 'USA'),
    )
    category = models.CharField(max_length=100, choices=COUNTRY, default='RU')

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
