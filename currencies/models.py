from django.db import models


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=5)
    central_bank = models.CharField(max_length=100)
    current_interest_rate = models.URLField()
    currency_history = models.TextField()
    picture = models.ImageField(upload_to='currency_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
