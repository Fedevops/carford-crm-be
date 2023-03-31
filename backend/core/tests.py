from django.test import TestCase
from .models import Car, Customer

class CarTestCase(TestCase):
    def test_car_creation(self):
        customer = Customer.objects.create(name='Fernando', email='fernandosilvadevops@gmail.com', phone='5547999911656')
        car = Car.objects.create(model='Mustang', year=2021, price=32000, type='sedan', owner=customer)
        self.assertEqual(car.model, 'Mustang')
        self.assertEqual(car.year, 2021)
        self.assertEqual(car.price, 32000)
        self.assertEqual(car.type, 'sedan')
        self.assertEqual(car.owner, customer)