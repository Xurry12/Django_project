from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Info(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='graphics_images')

class Top20(models.Model):
    year = models.IntegerField()
    table = RichTextField()
    image = models.ImageField(upload_to='graphics_images')


# class Analytics(models.Model):
#     title = models.TextField()
#     description = models.TextField()
#     graphic = models.ImageField(upload_to='graphics_images')



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


# class Statistics2(models.Model):
#     title = models.CharField(max_length=200)
#     content = RichTextField()
#     picture = models.ImageField(upload_to='graphics_images')
#     table = models.JSONField()

