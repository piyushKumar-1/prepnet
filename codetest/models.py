from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404



User = get_user_model()



GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]


# PROFILE MODEL MANAGER
class ProfileManager(models.Manager):
    def get_auth_profile(self, profile, user, *args, **kwargs):
        return get_object_or_404(self, pk=profile, user=user)

    def check_auth_profile(self, user, *args, **kwargs):
        try:
            obj = self.get(user=user)
            if obj:
                return obj
        except Trying.DoesNotExist:
            return None


# PROFILE MODEL
class Trying(models.Model):
    user = models.OneToOneField(
        User,
        default=1,
        on_delete=models.CASCADE
    )
    username = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()


