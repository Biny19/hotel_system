from django.contrib import admin
from .models import Reservation, ContactMessage

admin.site.register(Reservation)
admin.site.register(ContactMessage)
