from django.db import models

class Post(models.model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title
        
