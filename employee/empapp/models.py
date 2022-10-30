from django.db import models


class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    rno = models.IntegerField()




