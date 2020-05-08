from django import forms
from .models import New_Project, Comment





class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]

# DataFlair #File_Upload
class Entry_form(forms.ModelForm):
    Project_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'What do you call your invention??',
            }
        )
    )

    technologies = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': "Python, Flask(seperated by ,)"
            }
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Describe yout project...'
            }
        )
    )

    class Meta:
        model = New_Project
        fields = [
            'Project_Name',
            'technologies',
            'display_picture',
            'description'
        ]