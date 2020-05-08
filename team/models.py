from django.db import models
from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()



class Team_req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    team_name = models.CharField(max_length=25)
    team_size = models.IntegerField()
    working_on = models.CharField(max_length=400)


class Team_skill(models.Model):
    team = models.ForeignKey(Team_req, on_delete=models.CASCADE, default=1)
    member_skill = models.CharField(max_length=100)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
