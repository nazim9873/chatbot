from django.db import models

# Create your models here.
class Intent(models.Model):
  trigger=models.CharField(max_length=500,null=True)
  response=models.CharField(max_length=500,null=True)
  def __str__(self):
    return self.trigger
