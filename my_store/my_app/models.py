from django.db import models

# Create your models here.

class Vehicle(models.Model):
    # Choices for vehicle types
    VEHICLE_TYPES = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle'),
    ]

    # Type of vehicle
    type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    # Number of vehicles in stock
    number_in_stock = models.PositiveIntegerField()
    # Price of the vehicle
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Color of the vehicle (optional)
    color = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        # String representation of the vehicle
        return f"{self.type.capitalize()} - {self.color or 'No color'}"


class Customer(models.Model):
    # Name of the customer
    name = models.CharField(max_length=100)

    def __str__(self):
        # String represntation of the customer
        return self.name

class CustomerOrder(models.Model):
    # Customer who placed the order
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Vehicles included in the order
    vehicles = models.ManyToManyField(Vehicle, through='OrderItem')
    # Date and time when the order was created
    created_date = models.DateTimeField(auto_now_add=True)
    # Wheather the order has been paid or not
    paid = models.BooleanField(default=False)

    def __str__(self):
        # String representation of the order
        return f"Order #{self.id} by {self.customer.name}"

class OrderItem(models.Model):
    # Order to which the item belongs
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    # Vehicle included in the order item
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    # Quantity of the vehicle in the order item
    quantity = models.PositiveIntegerField()

    def __str__(self):
        # String representation of the order item
        return f"{self.quantity} x {self.vehicle.type}"