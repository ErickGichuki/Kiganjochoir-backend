from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField()

class RecordedSongs(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='')
