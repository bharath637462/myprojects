from django.db import models
from colorfield.fields import ColorField



class user(models.Model):
    # userid = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    color = ColorField(default='#FF0000')


    def __str__(self):
        return self.first_name
