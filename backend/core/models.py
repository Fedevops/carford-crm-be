from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Car(models.Model):
    TYPE_CHOICES = (
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('convertible', 'Convertible'),
        ('suv', 'SUV')
    )
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=11, choices=TYPE_CHOICES, blank=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model