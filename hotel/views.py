from django.shortcuts import render, redirect
from .forms import ReservationForm, ContactForm

def reservation_form(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')  # Redirect to success page
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})
def __str__(self):
    return self.name

def contact_form(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
def __str__(self):
    return self.name

def reservation_success(request):
    return render(request, 'index.html')

def contact_success(request):
    return render(request, 'index.html')
def home_page(request):
    return render(request, 'index.html')

