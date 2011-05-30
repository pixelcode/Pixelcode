from django.contrib.auth.models import User
from django import forms
from models import *

class ContactUsForm(forms.ModelForm):                  
    class Meta:
        model = ContactUs
        exclude = ('publish_date')