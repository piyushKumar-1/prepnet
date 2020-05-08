from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


class New_Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Project_Name = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    description = models.TextField(max_length=1500, default='')
    display_picture = models.FileField()


    def __str__(self):
        return self.Project_Name



class CommentManager(models.Manager):

    def create_comment(self, project, user):
        comment = self.create(post=project, owner=user)
        comment.save()

    def get_comment(self, p_id, c_id, user):
        return get_object_or_404(self, post=p_id, pk=c_id, owner=user)



class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    project = models.ForeignKey(New_Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return self.comment

