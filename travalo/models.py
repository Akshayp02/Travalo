
from django.db import models
from django.forms import CharField

# Create your models here.
class Destinations(models.Model):
    
    name = models.CharField(max_length=100)
    discr = models.TextField()
    img = models.ImageField(upload_to ="pics")
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
