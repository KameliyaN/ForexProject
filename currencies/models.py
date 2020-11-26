from django.db import models


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    central_bank = models.CharField(max_length=100)
    current_interest_rate = models.URLField()
    currency_history = models.TextField()
    picture = models.ImageField(upload_to='currency_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Links(models.Model):
    description = models.CharField(max_length=200)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'I`m in {self.category.name} category'
