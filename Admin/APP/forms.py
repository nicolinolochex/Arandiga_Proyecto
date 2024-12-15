from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a valid email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }
        error_messages = {
            'name': {'required': 'Please enter your name.'},
            'email': {'required': 'Please enter your email.'},
            'phone': {'required': 'Please enter your phone number.'},
            'message': {'required': 'Please enter your message.'},
        }
