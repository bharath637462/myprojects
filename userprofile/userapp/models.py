from django.db import models


class user(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class userprofile(models.Model):
    user = models.ForeignKey(user, related_name='users', on_delete=models.CASCADE)
    job = models.CharField(max_length=30)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.job
