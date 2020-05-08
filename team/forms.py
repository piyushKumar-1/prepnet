from django import forms
from .models import Team_req, Team_skill


class Team_ticket(forms.ModelForm):
    team_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Team Name'
            }
        )
    )

    team_size = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Team Size'
            }
        )
    )

    working_on = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'IOT, AI, AUTOMATION etc.'
            }
        )
    )


    class Meta:
        model = Team_req
        fields = ('team_name', 'team_size', 'working_on')

    def clean_team_size(self, *args, **kwargs):
        team_size = self.cleaned_data.get('team_size')
        if team_size > 10:
            raise forms.ValidationError('Team size must be below 10!')
        elif team_size < 2:
            raise forms.ValidationError('Team size must be at least 2!')
        else:
            return team_size


class Member_skills(forms.ModelForm):
    member_skill = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Skill required'
            }
        )
    )



    class Meta:
        model = Team_skill
        fields = ('member_skill',)

