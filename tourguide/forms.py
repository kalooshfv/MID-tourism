from django import forms
from .models import Task
from django.forms import TextInput

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields=["date","destination",]
        widgets = {
            'date':TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Task Title'
                }), 
            'destination':TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Description'
                })
        }