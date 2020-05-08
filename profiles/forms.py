from django import forms
from .models import Profile

GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Name'
            }
        )
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Age'
            }
        )
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Country'
            }
        )
    )

    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Skills'
            }
        )
    )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Country',
                'rows': 4
            }
        )
    )
    display_picture = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('name', 'age', 'gender', 'location', 'skills', 'bio', 'display_picture')

    def clean_age(self, *args, **kwargs):
        age = self.cleaned_data.get('age')
        if age > 50:
            raise forms.ValidationError('Age must be belove 50 years!')
        elif age < 18:
            raise forms.ValidationError('Age must be at least 18 years!')
        else:
            return age
