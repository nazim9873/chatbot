from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Intent(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  trigger=models.CharField(max_length=500,null=True)
  response=models.CharField(max_length=500,null=True)

  def __str__(self):
    return self.trigger
