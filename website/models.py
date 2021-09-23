from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=10)
    age = models.IntegerField()



#ism va familyasi bn kursatib turadi admin faylga
    def __str__(self) -> str:
        return self.fname + ' ' + self.lname + " " + self.email