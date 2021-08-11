from django.db import models

# Create your models here.
class Userprofile(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=20)


    def __str__(self):
        return self.firstname
