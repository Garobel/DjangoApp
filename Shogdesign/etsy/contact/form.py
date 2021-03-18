from typing import Tuple

from django import forms
from .models import users_contact

class Contact (forms.ModelForm):

    class Meta:

        model = users_contact

        fields = ('name','email','message')





