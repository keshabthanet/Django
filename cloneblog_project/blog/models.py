from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(null=True)
    auther= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
     post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
     author = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     approved_comment = models.BooleanField(default=False)

     def __str__(self): 
        return 'Comment by {} on {}'.format(self.author, self.post)


