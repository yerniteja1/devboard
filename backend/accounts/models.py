from django.db import models
from django.db import AbstractUser

class User(AbstractUser):
  avatar = models.URLField(blank=True, null=True)
  bio = models.TextField(blank=True)
  
  class Meta:
    db_table = 'users'
    
  def __str__(self):
    return self.email