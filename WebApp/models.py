from django.db import models

# Create your models here.
class Emp(models.Model):
    Name = models.CharField(max_length=30)
    Salary = models.IntegerField()