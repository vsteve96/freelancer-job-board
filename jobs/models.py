from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="job_posts",
    null=True,  # allow NULL in the database
    blank=True  # allow leaving it empty in forms/admin
)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    def __str__(self):
        return self.title