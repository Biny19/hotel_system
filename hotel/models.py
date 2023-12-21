from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    room_type = models.CharField(max_length=50)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=False, default='')
    email = models.EmailField()
    message = models.TextField()