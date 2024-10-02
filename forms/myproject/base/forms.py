from django import forms
from .models import Post

class Contact(forms.ModelForm):
    class Meta:
        model = Post  
        fields = ['name', 'desc']
