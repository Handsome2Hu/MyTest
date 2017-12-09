from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()