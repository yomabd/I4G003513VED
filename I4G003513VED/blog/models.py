from cgitb import text
from email.policy import default
# from django.conf import settings
from django.db import models
from django.forms import CharField
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200); 
    Text = models.TextField()
    Author = models.ForeignKey(User , on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.Title} --> {self.Text} --> {self.Author}" 



    
