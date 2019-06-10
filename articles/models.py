from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Article(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
