from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    featured_image = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.title