from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.IntegerField()
    family = models.ForeignKey('Family', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

