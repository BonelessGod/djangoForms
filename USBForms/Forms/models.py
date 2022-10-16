from django.db import models

# Create your models here.

class Inscriptions(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    age = models.IntegerField

    def __str__(self):
        return f'{self.firstName} {self.lastName}'