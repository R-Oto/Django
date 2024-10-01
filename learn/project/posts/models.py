from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title