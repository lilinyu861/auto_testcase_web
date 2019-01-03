from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    # phone = models.IntegerField(max_length=11)
    # email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
