from django import forms
from .models import Reservation, ContactMessage

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class ContactForm(forms.ModelForm):  
    class Meta:
        model = ContactMessage
        fields = '__all__'