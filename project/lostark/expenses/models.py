from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    # for sorting data according to date in descending order
    class Meta:
        ordering = ['-date']

class Category(models.Model):
    name = models.CharField(max_length = 255)

    # defining how this model should be called in plural form (ie categorys vs categories)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name