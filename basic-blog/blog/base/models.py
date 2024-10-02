from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    img = models.ImageField(upload_to='posts')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title