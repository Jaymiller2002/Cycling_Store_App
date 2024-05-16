from django.db import models

# Create your models here.

class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle')
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    number_in_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color = models.CharField(max_length=50, blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ManyToManyField(Vehicle)
    created_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)

    def calculate_total_price(self):
        total_price = sum(vehicle.price for vehicle in self.order.all())
        self.total_price = total_price
        self.save()

    def __str__(self):
        return f"Order ID: {self.id}, Customer: {self.customer.name}, Total Price: {self.total_price}"
