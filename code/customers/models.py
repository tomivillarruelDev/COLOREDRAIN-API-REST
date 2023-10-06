from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name
