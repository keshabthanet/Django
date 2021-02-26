from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.TextField(max_length=200)
    
