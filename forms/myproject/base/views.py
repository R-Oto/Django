from django.shortcuts import render, redirect
from . import forms

def index(request):
    if request.method == 'POST':
        form = forms.Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = forms.Contact()
    
    return render(request, 'index.html', {'form': form})
