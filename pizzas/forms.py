from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class META: 
        model = Topping
        fields = ['text']
        labels = {'comments:' ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}