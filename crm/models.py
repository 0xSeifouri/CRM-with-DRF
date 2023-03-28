from django.db import models


class CustomerData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



