from django import forms
from django.forms import widgets
from about.models import UserSuggestion

class CustomContactForm(forms.ModelForm):
    class Meta:
        model = UserSuggestion
        fields = "__all__"
        widget = {
            'full_name': forms.TextInput(
                attrs={
                    'class':'form-controller',
                    'placeholder': 'Full name',
                    'required': 'true'
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class':'form-controller',
                    'placeholder': 'Full name',
                    'required': 'true'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class':'form-controller',
                    'placeholder': 'Full name',
                    'required': 'true'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class':'form-controller',
                    'placeholder': 'Full name',
                    'required': 'true'
                }
            )
        }