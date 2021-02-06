from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="blog/image",blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
