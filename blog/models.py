from unittest import defaultTestLoader
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  date_published = models.DateTimeField('date published')
  date_updated = models.DateTimeField('date updated')
  content = models.TextField(editable=True)
  is_published = models.BooleanField()
  likes = models.IntegerField(default=0)

  def __str__(self):
      return self.title

class Tag(models.Model):
  name = models.CharField(max_length=200, unique=True)
  
  def __str__(self):
    return self.name

class Comment(models.Model):
  comment = models.TextField()
  date_published = models.DateTimeField()

  def __str__(self):
    return self.comment

class Tagged(models.Model):
  post = models.ForeignKey(Post, on_delete=models.PROTECT)
  tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

class Commented(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

