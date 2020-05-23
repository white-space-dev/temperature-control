from django.db import models
from random import randint
from datetime import date
import django
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Personnel(models.Model):
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, blank=True)
    date_signedoff = models.DateField(null=True, blank=True)
    onboard = models.BooleanField(null=True)

    # am_pm = models.ForeignKey(AM_PM, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_onboard(self):
        if self.date_joined < date.today < self.date_signedoff:
            self.onboard = True
        return self.onboard


class Temperature(models.Model):
    user = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    temp_AM = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    temp_PM = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    date_temp_taken = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.name

    class Meta:
        unique_together = [['user', 'date_temp_taken']]


