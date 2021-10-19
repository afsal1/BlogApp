from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE)


class ImageMedia(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    friend = models.ForeignKey(
        User, related_name='friend_user', on_delete=models.CASCADE)


class VideoMedia(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    friend = models.ForeignKey(
        User, related_name='video_friend_user', on_delete=models.CASCADE)
