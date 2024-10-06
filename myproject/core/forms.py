from .models import *
from django import forms

class MenuForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(widget=forms.NumberInput)
        
SHIFTS = (
    ("1", 'mo'),
    ("2", 'tu'),
    ("3", 'we'),
    ("4", 'th'),
    ("5", 'fr'),
    ("6", 'sa'),
    ("7", 'su'),
)

class InputForm(forms.Form):
    first = forms.CharField(max_length=200)
    last = forms.CharField(max_length=200)
    shifts = forms.ChoiceField(choices=SHIFTS)