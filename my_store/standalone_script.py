import os
import django
from django.conf import settings
from my_store import *
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "my_store.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW


# This import simplifies the creation of custom management commands in Django by providing common functionality and structure
# Importing BaseCommand class from Django's management framework
# This import statement allows you to access and use the BaseCommand class provided by Django's management framework.
# BaseCommand is a base class for creating custom management commands in Django.
# By importing BaseCommand, you can subclass it to define custom management commands tailored to your project's needs.
# These custom commands can perform various tasks such as database operations, data manipulation, and other management tasks.
from django.core.management.base import BaseCommand

# Import models from my_app
from my_app.models import Vehicle, Customer, CustomerOrder, OrderItem

# Made a new class Named Command to handle various differnt things
class Command(BaseCommand):
    help = 'Manage the cycling store'

    def handle(self, *args, **kwargs):
        self.main_menu()

    def main_menu(self):
        while True:
            print("\n\033[97mCycling Store Management 🚲🛠️\033[0m")
            menu_options = {
                '1': 'Order more Vehicles 🚗',
                '2': 'Create a new Customer 👤',
                '3': 'Create a new Customer Order 👤📦',
                '4': 'Display Inventory 🛒',
                '5': 'Cancel a Customer Order ❌',
                '6': 'Mark an Order as Paid 💳',
                '7': 'Display Order History for a customer 🛒👤',
                '8': 'Exit ❌'
            }
            for key, value in menu_options.items():
                print(f"\033[95m{key}. {value}\033[0m")
            choice = input("\033[92mSelect an option: \033[0m").strip()

            actions = {
                '1': self.order_more_vehicles,
                '2': self.create_new_customer,
                '3': self.create_customer_order,
                '4': self.display_inventory,
                '5': self.cancel_customer_order,
                '6': self.mark_order_paid,
                '7': self.display_order_history,
                '8': lambda: exit()
            }
            if choice in actions:
                actions[choice]()
            else:
                print("\033[91mInvalid choice, please try again.\033[0m")
    
    def clear_database(self):
        models = [Vehicle, Customer, CustomerOrder, OrderItem]
        for model in models:
            if model.objects.exists():  # Check if there are any objects before deleting
                model.objects.all().delete()

    def order_more_vehicles(self):
        vehicle_type = input("\033[95mEnter vehicle type (unicycle, bicycle, tricycle): \033[0m").strip().lower()
        quantity = self.get_positive_integer("\033[95mEnter quantity: \033[0m")
        price = self.get_positive_float("\033[95mEnter price: \033[0m")
        color = input("\033[95mEnter color: \033[0m").strip()

        try:
            vehicle = Vehicle.objects.get(type=vehicle_type)
            vehicle.number_in_stock += quantity
        except Vehicle.DoesNotExist:
            vehicle = Vehicle(type=vehicle_type, number_in_stock=quantity, price=price, color=color)
        vehicle.save()
        print(f"\033[92mUpdated stock for {vehicle_type}: {vehicle.number_in_stock}\033[0m")

    def create_new_customer(self):
        name = input("\033[95mEnter customer name: \033[0m").strip()
        Customer.objects.create(name=name)
        print(f"\033[92mCustomer {name} created.\033[0m")

    def create_customer_order(self):
        customer_name = input("\033[95mEnter customer name: \033[0m").strip()
        try:
            customer = Customer.objects.get(name=customer_name)
        except Customer.DoesNotExist:
            print(f"\033[91mNo customer found with name {customer_name}\033[0m")
            return
        order = CustomerOrder.objects.create(customer=customer)
        while True:
            vehicle_type = input("\033[95mEnter vehicle type to order (or 'done' to finish): \033[0m").strip().lower()
            if vehicle_type == 'done':
                break
            try:
                vehicle = Vehicle.objects.get(type=vehicle_type)
                if vehicle.number_in_stock > 0:
                    quantity = self.get_positive_integer("\033[95mEnter quantity: \033[0m")
                    if quantity <= vehicle.number_in_stock:
                        OrderItem.objects.create(order=order, vehicle=vehicle, quantity=quantity)
                        vehicle.number_in_stock -= quantity
                        vehicle.save()
                        print(f"\033[92mAdded {quantity} {vehicle_type}(s) to order\033[0m")
                    else:
                        print(f"\033[91mNot enough stock for {quantity} {vehicle_type}(s). Only {vehicle.number_in_stock} left.\033[0m")
                else:
                    print(f"\033[91mNo stock available for {vehicle_type}.\033[0m")
            except Vehicle.DoesNotExist:
                print(f"\033[91mNo vehicle found with type {vehicle_type}\033[0m")
        print(f"\033[92mOrder created with ID: {order.id}\033[0m")

    def display_inventory(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print("\n\033[94mCurrent Inventory:\033[0m")
        for vehicle in Vehicle.objects.all():
            print(f"{vehicle.type.capitalize()}: {vehicle.number_in_stock} in stock, ${vehicle.price}, Color: {vehicle.color or 'No color'}")

    def cancel_customer_order(self):
        order_id = self.get_positive_integer("\033[91mEnter order ID to cancel: \033[0m")
        try:
            order = CustomerOrder.objects.get(id=order_id)
            for item in order.orderitem_set.all():
                vehicle = item.vehicle
                vehicle.number_in_stock += item.quantity
                vehicle.save()
            order.delete()
            print(f"\033[91mOrder {order_id} cancelled and stock updated.\033[0m")
        except CustomerOrder.DoesNotExist:
            print(f"\033[91mNo order found with ID {order_id}\033[0m")

    def mark_order_paid(self):
        order_id = self.get_positive_integer("\033[93mEnter order ID to mark as paid: \033[0m")
        try:
            order = CustomerOrder.objects.get(id=order_id)
            order.paid = True
            order.save()
            print(f"\033[92mOrder {order_id} marked as paid.\033[0m")
        except CustomerOrder.DoesNotExist:
            print(f"\033[91mNo order found with ID {order_id}\033[0m")

    def display_order_history(self):
        customer_name = input("\033[94mEnter customer name: \033[0m").strip()
        try:
            customer = Customer.objects.get(name=customer_name)
            orders = CustomerOrder.objects.filter(customer=customer)
            if orders.exists():
                print(f"\033[94mOrder history for {customer.name}:\033[0m")
                for order in orders:
                    print(f"Order ID: {order.id}, Paid: {'Yes' if order.paid else 'No'}, Created Date: {order.created_date}")
                    for item in order.orderitem_set.all():
                        print(f" - {item.quantity} x {item.vehicle.type}")
            else:
                print(f"\033[91mNo orders found for {customer.name}.\033[0m")
        except Customer.DoesNotExist:
            print(f"\033[91mNo customer found with name {customer.name}\033[0m")

    def get_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("\033[91mPlease enter a positive integer.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a positive integer.\033[0m")

    def get_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("\033[91mPlease enter a positive number.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a positive number.\033[0m")

command = Command()
command.handle()



