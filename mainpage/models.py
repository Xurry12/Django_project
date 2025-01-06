from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Info(models.Model):
    name = models.TextField()
    description = RichTextField()
    image = models.ImageField(upload_to='graphics_images')

class Top20(models.Model):
    year = models.IntegerField()
    table = RichTextField()
    image = models.ImageField(upload_to='graphics_images')

class Top20Analytic(models.Model):
    year = models.IntegerField()
    table = RichTextField()
    image = models.ImageField(upload_to='graphics_images')

class Statistics(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    picture = models.ImageField(upload_to='graphics_images')

    def __str__(self):
        return self.title


class Geography(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    picture = models.ImageField(upload_to='graphics_images')

    def __str__(self):
        return self.title

class Relevance(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    picture = models.ImageField(upload_to='graphics_images')

    def __str__(self):
        return self.title



