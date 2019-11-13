from django.db import models

# Create your models here.
class state(models.Model):
     sname=models.CharField(max_length=255,primary_key=True)
def __str__(self):
 return self.sname
class capitalcity(models.Model):
    cname=models.CharField(max_length=255,primary_key=True)
    state=models.OneToOneField(state,on_delete=models.CASCADE,)
def __str__(self):
 return self.cname