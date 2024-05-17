from django.db import models

# Create your models here.

# Define Vehicle model
# class Vehicle(models.Model):
#     TYPE_CHOICES = [
#         ('unicycle', 'Unicycle'),
#         ('bicycle', 'Bicycle'),
#         ('tricycle', 'Tricycle')
#     ]
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     number_in_stock = models.IntegerField(default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     color = models.CharField(max_length=50, blank=True)

# # Define Customer model
# class Customer(models.Model):
#     name = models.CharField(max_length=100)

# # Define CustomerOrder model
# class CustomerOrder(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order = models.ManyToManyField(Vehicle)
#     created_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     paid = models.BooleanField(default=False)

#     def calculate_total_price(self):
#         total_price = sum(vehicle.price for vehicle in self.order.all())
#         self.total_price = total_price
#         self.save()

#     def __str__(self):
#         return f"Order ID: {self.id}, Customer: {self.customer.name}, Total Price: {self.total_price}"

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle'),
    ]

    type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    number_in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.type.capitalize()} - {self.color or 'No color'}"


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicles = models.ManyToManyField(Vehicle, through='OrderItem')
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.vehicle.type}"