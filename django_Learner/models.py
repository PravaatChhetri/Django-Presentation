from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.
class Info(models.Model):
    
    name =models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    College_Name=models.TextField(default="College of Science and Technology")