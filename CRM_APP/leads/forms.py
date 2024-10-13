# forms.py
from django import forms
from .models import Leads

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['name', 'email', 'description', 'status', 'priority']  # Specify the fields you want in the form
