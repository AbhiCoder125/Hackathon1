from django.db import models

class User(models.Model):
    Uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    Location = models.TextField()
    
     
    
    