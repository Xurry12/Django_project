from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='graphics_images')