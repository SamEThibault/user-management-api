from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400, blank=True, default="")
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.title)