from django import forms
from .models import Trying

GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]


class TryingForm(forms.ModelForm):
    class Meta:
        model = Trying
        fields = \
        ('username',)
