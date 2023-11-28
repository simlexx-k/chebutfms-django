from django import forms
from .models import TeaSubmission

class TeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = TeaSubmission
        fields = ['field_manager', 'farmer', 'amount_in_kgs']
