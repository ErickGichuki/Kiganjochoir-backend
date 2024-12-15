from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary
import cloudinary.uploader

class Songs(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField()

from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader

class RecordedSongs(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='choir-audio/', storage=MediaCloudinaryStorage())

    def save(self, *args, **kwargs):
        if self.audio:
            # Upload the file to Cloudinary and get the URL
            upload_result = cloudinary.uploader.upload(self.audio, resource_type='auto')

            # Save the Cloudinary URL to the 'audio' field (or you can store the 'secure_url' or 'public_id')
            self.audio = upload_result['secure_url']  # or use 'upload_result['public_id']' if you prefer
        super().save(*args, **kwargs)

