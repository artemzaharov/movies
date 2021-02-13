#we create this file to work with django forms
from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        fields = ('name','email','text')

