from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Facebook(models.Model):
    title = models.CharField(max_length=40)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    fb_id = models.CharField(max_length=20)
    access_token = models.CharField(max_length=255)
    expires_in = models.DateTimeField()
