from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class cars:
    name: str
    year: str
    model: str
    cost: int
    img:str
    offer:bool

class carsfromdatabaser(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField(default=0)
    model=models.CharField(max_length=100)
    desc=models.TextField(default='')
    cost=models.IntegerField(default=0)
    img=models.ImageField(upload_to = 'pics')
    offer=models.BooleanField(default=False)