from django.db import models
from django.utils import timezone
# Create your models here.


class Deal(models.Model):
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True)
    reply_count = models.IntegerField()
    up_count = models.IntegerField()
    created_at = models.DateTimeField(default=timezone())