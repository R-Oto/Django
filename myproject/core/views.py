from django.shortcuts import render
from django.http import HttpResponse
from .forms import MenuForm, InputForm
# Create your views here.
def index(req):
    if req.method == "POST":
        form = MenuForm
    return render(req, 'index.html', {'form':form})

def shifts(req):
    form = InputForm
    return render(req, 'shifts.html', {'form':form})