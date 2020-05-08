from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]


class ProfileManager(models.Manager):
    def get_auth_profile(self, profile, user, *args, **kwargs):
        return get_object_or_404(self, pk=profile, user=user)

    def check_auth_profile(self, user, *args, **kwargs):
        try:
            obj = self.get(user=user)
            if obj:
                return obj
        except Profile.DoesNotExist:
            return None

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, default=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=100, default='USA')
    skills = models.CharField(max_length=120, choices=None)
    bio = models.TextField(blank=True, default='Hello buddies..!')
    display_picture = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

