from django.db import models
from embed_video.fields import EmbedVideoField

class mysigninform(models.Model):
    Username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    class Meta:
        db_table = 'signin'

class Registermovie(models.Model):
    Name = models.CharField(max_length=30)
    Year = models.IntegerField()
    categories = models.CharField(max_length=30)
    Durection = models.CharField(max_length=20)
    descriptions =models.CharField(max_length=1000)
    image = models.ImageField(upload_to='movie')
    video = models.FileField(upload_to='video')
    

    def __str__(self):
        return f"{self.Name}"
    class Meta:
        db_table = 'movies'