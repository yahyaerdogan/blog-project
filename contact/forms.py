from django import forms
from django.db import models
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=["name", "email", "phone", "message"]