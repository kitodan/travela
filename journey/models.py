from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Trip(models.Model):
    depature = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=True)
    date_travel = models.TextField(max_length=10)
    time_travel = models.CharField(max_length=6)
    amount = models.IntegerField(default = 0)
    seats = models.IntegerField(default = 0)
    number_seats = models.CharField(max_length=3)
    ride_detail = models.TextField(max_length=200)
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.depature

    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'pk':self.pk})

