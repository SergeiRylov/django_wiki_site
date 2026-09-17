from django import forms
from django.contrib.auth.models import User


class IndexForm(forms.Form):

    first_name = forms.CharField(label='Username', required=True)
    birthday  = forms.DateField(label='Birthday', required=False)
