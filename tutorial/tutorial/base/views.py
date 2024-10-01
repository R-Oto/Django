from django.shortcuts import render, redirect
from .models import Tour
from .forms import ContactForm
# Create your views here.
def index(request):
    tours = Tour.objects.all()
    return render(request, 'tours/index.html', {'tours':tours})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'tours/contact.html', {'form':form})

def contact_success_view(request):
    return render(request, 'tours/contact_success.html')