from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    blog_image = models.FileField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
