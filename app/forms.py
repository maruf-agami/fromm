from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Formfillup


# Create your forms here.
class FormfillupForm(forms.ModelForm):
    class Meta:
        model = Formfillup
        exclude = (
            'step',
            'dept_signature',
            'provost_signature',
            'register_signature',
            'payable_amount',
            'user',
        )