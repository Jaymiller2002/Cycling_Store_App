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
    # Help message for the command
    help = 'Manage the cycling store'

    # Method called when the command is executed
    def handle(self, *args, **kwargs):
        # 'self' is a reference to the current instance of the class.
        # It is used to access variables and methods within the class.
        # Here, 'handle' is a method of the Command class, and 'self' allows
        # us to access other methods like 'clear_database' and 'main_menu'.
        # '*args' is used to pass a variable number of positional arguments to a function.
        # In this case, it allows the 'clear_database' method to accept any number of
        # positional arguments, although it doesn't use them in this specific implementation.
        # Clear the database before starting
        self.clear_database()
        # Display the main menu
        self.main_menu()

    # Method to clear all tables in the database before running the script
    # Had to do this because it was printing multiple ids, names and ect.. This is the only way I found to handle that error
    def clear_database(self):
        Vehicle.objects.all().delete()
        Customer.objects.all().delete()
        CustomerOrder.objects.all().delete()
        OrderItem.objects.all().delete()

    # Method to dsiplay and manage the main menu
    def main_menu(self):
        while True:
            # Print the main menu with color formatting
            print("\n\033[97mCycling Store Management 🚲🛠️\033[0m")
            print("\033[95m1. Order more Vehicles 🚗\033[0m")
            print("\033[95m2. Create a new Customer 👤\033[0m")
            print("\033[95m3. create a new Customer Order 👤📦\033[0m")
            print("\033[94m4. Display Inventory 🛒\033[0m")
            print("\033[91m5. Cancel a Customer Order ❌\033[0m")
            print("\033[92m6. Mark an Order as Paid 💳\033[0m")
            print("\033[94m7. Display Order History for a customer 🛒👤\033[0m")
            print("\033[91m8. Exit ❌\033[0m")
            choice = input("\033[92mSelect an option: \033[0m")
            
            # Execute the corresponding action based on user input
            if choice == '1':
                self.order_more_vehicles()
            elif choice == '2':
                self.create_new_customer()
            elif choice == '3':
                self.create_customer_order()
            elif choice == '4':
                self.display_inventory()
            elif choice == '5':
                self.cancel_customer_order()
            elif choice == '6':
                self.mark_order_paid()
            elif choice == '7':
                self.display_order_history()
            elif choice == '8':
                break
            else:
                print("\033[91mInvalid choice, please try again.\033[0m")
    
    # Method to order more vehicles
    def order_more_vehicles(self):
        # Get input from user for vehicle details
        # .Strip() is used for specific error handling. It is a string method used to remove leading and trailing whitespace characters from a string.
        vehicle_type = input("\033[95mEnter vehicle type (unicycle, bicycle, tricycle): \033[0m").strip().lower()
        quantity = self.get_positive_integer("\033[95mEnter quantity: \033[0m")
        price = self.get_positive_float("\033[95mEnter price: \033[0m")
        color = input("\033[95mEnter color: \033[0m").strip()

        # Update the database with the new vehicle information
        try:
            vehicle = Vehicle.objects.get(type=vehicle_type)
            vehicle.number_in_stock += quantity
        except Vehicle.DoesNotExist:
            vehicle = Vehicle(type=vehicle_type, number_in_stock=quantity, price=price, color=color)
        vehicle.save()
        print(f"\033[92mUpdated stock for {vehicle_type}: {vehicle.number_in_stock}\033[0m")

    # Method to create a new customer
    def create_new_customer(self):
        # Get input from user for customer name
        name = input("\033[95mEnter customer name: \033[0m").strip()
        # Create a new customer object and save it to the database
        Customer.objects.create(name=name)
        print(f"\033[92mCustomer {name} created.\033[0m")

    # Method to create a new customer order
    def create_customer_order(self):
        # Get input from user for customer name
        customer_name = input("\033[95mEnter customer name: \033[0m").strip()
        try:
            # Get the customer object from the database
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
                # Create a new order item and update stock
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
    # Method to display inventory
    def display_inventory(self):
        print("\n\033[94mCurrent Inventory:\033[0m")
        for vehicle in Vehicle.objects.all():
            print(f"{vehicle.type.capitalize()}: {vehicle.number_in_stock} in stock, ${vehicle.price}, Color: {vehicle.color or 'No color'}")
    # Method to cancel a customer order
    def cancel_customer_order(self):
        order_id = self.get_positive_integer("\033[91mEnter order ID to cancel: \033[0m")
        try:
            # Get the order object from the database
            order = CustomerOrder.objects.get(id=order_id)
            # Restock stock for each item in the order
            for item in order.orderitem_set.all():
                vehicle = item.vehicle
                vehicle.number_in_stock += item.quantity
                vehicle.save()
            # Delete the order
            order.delete()
            print(f"\033[91mOrder {order_id} cancelled and stock updated.\033[0m")
        except CustomerOrder.DoesNotExist:
            print(f"\033[91mNo order found with ID {order_id}\033[0m")
    # Method to mark order as paid
    def mark_order_paid(self):
        order_id = self.get_positive_integer("\033[93mEnter order ID to mark as paid: \033[0m")
        try:
            # Get the order object from the database
            order = CustomerOrder.objects.get(id=order_id)
            # Mark tbe order as paid
            order.paid = True
            order.save()
            print(f"\033[92mOrder {order_id} marked as paid.\033[0m")
        except CustomerOrder.DoesNotExist:
            print(f"\033[91mNo order found with ID {order_id}\033[0m")
    # Method to display order history for a customer
    def display_order_history(self):
        customer_name = input("\033[94mEnter customer name: \033[0m").strip()
        try:
            # Get the customer object from the database
            customer = Customer.objects.get(name=customer_name)
            # Get all orders associated with the customer
            orders = CustomerOrder.objects.filter(customer=customer)
            if orders.exists():
                print(f"\033[94mOrder history for {customer.name}:\033[0m")
                # Display details of each order
                for order in orders:
                    print(f"Order ID: {order.id}, Paid: {'Yes' if order.paid else 'No'}, Created Date: {order.created_date}")
                    for item in order.orderitem_set.all():
                        print(f" - {item.quantity} x {item.vehicle.type}")
            else:
                print(f"\033[91mNo orders found for {customer.name}.\033[0m")
        except Customer.DoesNotExist:
            print(f"\033[91mNo customer found with name {customer.name}\033[0m")
    # Method to get a positive integer from user input
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
    # Method to get a positive float from user input
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

# Call it so it outputs text to the terminal
if __name__ == "__main__":
    command = Command()
    command.handle()


