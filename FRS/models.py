from django.db import models

# Create your models here.


class Flight(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    scheduled_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    fare = models.BigIntegerField()
    duration = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'Flights'
    
    def __str__(self):
        return self.name