# forms.py
from django import forms
from .models import TeaSubmission

class TeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = TeaSubmission
        fields = ['user', 'farmer', 'amount_in_kgs']  # Add other fields as needed
