from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Info(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='graphics_images')


class Analytics(models.Model):
    title = models.TextField()
    description = models.TextField()
    graphic = models.ImageField(upload_to='graphics_images')



class Statistics(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    picture = models.ImageField(upload_to='graphics_images')

    def __str__(self):
        return self.title


class Statistics2(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    picture = models.ImageField(upload_to='graphics_images')
    table = models.JSONField()


import csv
import io

# class GraphData(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     graph_image = models.ImageField(upload_to='graphics_images')
#     csv_data = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     def get_table_data(self):
#         if self.csv_data:
#             csv_file = io.StringIO(self.csv_data)
#             reader = csv.DictReader(csv_file)
#             return list(reader)
#         return []
