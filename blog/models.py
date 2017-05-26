from django.db import models
from django.utils import timezone

class Tag(models.Model):
    slug=models.SlugField(unique=True,max_length=50)
    def __str__(self):
        return self.slug

class Post(models.Model):
    title=models.CharField(max_length=50,default="title")
    slug=models.SlugField(unique=True,default="title")
    body=models.TextField(default="body")
    img=models.ImageField(null=True,blank=True)
    create=models.DateTimeField(default=timezone.now)
    tag=models.ManyToManyField(Tag)
    published=models.BooleanField(default=True)

    class Meta:
        ordering=["-title"]
    def __str__(self):
        return self.title