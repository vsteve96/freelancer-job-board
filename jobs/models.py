from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
## Create a class named Post inheriting from the Model class
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title