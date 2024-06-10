from django.db import models

# Create your models here.

class Person (models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    age = models.IntegerField()


    def __str__(self):
        return f'{self.firstName} {self.lastName} - {self.age} '

