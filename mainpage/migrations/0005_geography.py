# Generated by Django 5.1.4 on 2024-12-27 18:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_statistics2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('picture', models.ImageField(upload_to='graphics_images')),
            ],
        ),
    ]
