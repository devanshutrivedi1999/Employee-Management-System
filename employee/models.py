from __future__ import unicode_literals
from django.db import models


# Create your models here.
class employee(models.Model):
    eid =models.CharField(max_length=50)
    ename =models.TextField(default='Mr.')
    eemail =models.CharField(max_length=50)
    eaddress= models.TextField(max_length=50)
    econtact =models.CharField(max_length=50)
    edesign =models.CharField(max_length=50)
    ecursal =models.CharField(max_length=50)
    edoj =models.CharField(max_length=50)
    ewexp =models.CharField(max_length=50)
    epcomp =models.CharField(max_length=50)
    edpt =models.CharField(max_length=50)
    eba =models.CharField(max_length=50,default="")
    

    def __str__(self):
        return str(self.pk)+' | '+self.ename
