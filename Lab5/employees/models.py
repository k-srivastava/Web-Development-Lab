import datetime

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

    def is_eligible_for_promotion(self):
        return self.date_of_joining <= timezone.now().date() - datetime.timedelta(days=365 * 5)
