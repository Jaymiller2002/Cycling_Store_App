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

from my_app.models import Vehicle, Customer, CustomerOrder

# Function to print separator in cyan blue
def print_separator():
    print("\033[96m" + "=" * 40 + "\033[0m")  # Cyan blue color

# Create instances of the Vehicle model
vehicles = [
    Vehicle.objects.create(type='unicycle', number_in_stock=5),
    Vehicle.objects.create(type='bicycle', number_in_stock=10),
    Vehicle.objects.create(type='tricycle', number_in_stock=8)
]

# Create instances of the Customer model
customers = [
    Customer.objects.create(name='Jay Miller'),
    Customer.objects.create(name='Drew Stratton')
]

# Create instances of the CustomerOrder model
orders = [
    CustomerOrder.objects.create(customer=customers[0], created_date='2004-05-18', paid=True),
    CustomerOrder.objects.create(customer=customers[1], created_date='2024-05-19', paid=False)
]

# Add vehicles to the orders
orders[0].order.set([vehicles[0], vehicles[1]])
orders[1].order.set([vehicles[2]])


# Function to print separator in cyan blue
def print_separator():
    print("\033[96m" + "=" * 40 + "\033[0m")  # Cyan blue color

# Function to display IDs for vehicles
def display_vehicle_ids():
    print("\033[96m" + "Vehicle IDs:" + "\033[0m")
    for idx, vehicle in enumerate(vehicles, start=1):
        print(f"\033[96m" + f"{idx}. ID: {vehicle.id}, Type: {vehicle.type}, Number in Stock: {vehicle.number_in_stock}" + "\033[0m")

# Function to display IDs for customers
def display_customer_ids():
    print("\033[96m" + "Customer IDs:" + "\033[0m")
    for idx, customer in enumerate(customers, start=1):
        print(f"\033[96m" + f"{idx}. ID: {customer.id}, Name: {customer.name}" + "\033[0m")

# Function to display IDs for customer orders
def display_order_ids():
    print("\033[96m" + "Order IDs:" + "\033[0m")
    for idx, order in enumerate(orders, start=1):
        print(f"\033[96m" + f"{idx}. ID: {order.id}, Customer: {order.customer.name}, Created Date: {order.created_date}, Paid: {order.paid}" + "\033[0m")

# Print IDs of vehicles
display_vehicle_ids()
# Print out the attributes of each vehicle in cyan blue
print_separator()
print("\033[96m" + "Vehicles:" + "\033[0m")
for vehicle in vehicles:
    print("\033[96m" + f"ID: {vehicle.id}, Type: {vehicle.type}, Number in Stock: {vehicle.number_in_stock}" + "\033[0m")
print_separator()

# Print IDs of customers
display_customer_ids()
# Print out the attributes of each customer in cyan blue
print("\033[96m" + "Customers:" + "\033[0m")
for customer in customers:
    print("\033[96m" + f"ID: {customer.id}, Name: {customer.name}" + "\033[0m")
print_separator()

# Print IDs of customer orders
display_order_ids()
# Print out the attributes of each customer order in cyan blue
print("\033[96m" + "Customer Orders:" + "\033[0m")
for order in orders:
    print("\033[96m" + f"ID: {order.id}, Customer: {order.customer.name}, Created Date: {order.created_date}, Paid: {order.paid}" + "\033[0m")
    print("\033[96m" + "Vehicles Ordered:" + "\033[0m")
    for vehicle in order.order.all():
        print("\033[96m" + f"- Type: {vehicle.type}, Number in Stock: {vehicle.number_in_stock}" + "\033[0m")
    print_separator()






# Print out the attributes of each vehicle in cyan blue
print_separator()
print("\033[96m" + "Vehicles:" + "\033[0m")
for vehicle in vehicles:
    print("\033[96m" + f"Type: {vehicle.type}, Number in Stock: {vehicle.number_in_stock}" + "\033[0m")
print_separator()

# Print out the attributes of each customer in cyan blue
print("\033[96m" + "Customers:" + "\033[0m")
for customer in customers:
    print("\033[96m" + f"Name: {customer.name}" + "\033[0m")
print_separator()

# Print out the attributes of each customer order in cyan blue
print("\033[96m" + "Customer Orders:" + "\033[0m")
for order in orders:
    print("\033[96m" + f"Customer: {order.customer.name}, Created Date: {order.created_date}, Paid: {order.paid}" + "\033[0m")
    print("\033[96m" + "Vehicles Ordered:" + "\033[0m")
    for vehicle in order.order.all():
        print("\033[96m" + f"- Type: {vehicle.type}, Number in Stock: {vehicle.number_in_stock}" + "\033[0m")
    print_separator()


# CRUD operations for Vehicle
def create_vehicle(type, number_in_stock, price, color):
    try:
        vehicle = Vehicle.objects.create(type=type, number_in_stock=number_in_stock, price=price, color=color)
        return True, "\033[92mVehicle created successfully.\033[0m"
    except Exception as e:
        return False, f"\033[91mFailed to create vehicle: {str(e)}\033[0m"

def update_vehicle(vehicle_id, **kwargs):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        for key, value in kwargs.items():
            setattr(vehicle, key, value)
        vehicle.save()
        return True, "\033[92mVehicle updated successfully.\033[0m"
    except Vehicle.DoesNotExist:
        return False, "\033[91mVehicle not found.\033[0m"

def delete_vehicle(vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.delete()
        return True, "\033[92mVehicle deleted successfully\033[0m"
    except Vehicle.DoesNotExist:
        return False, "\033[91mVehicle not found\033[0m"

# CRUD operations for Customer
def create_customer(name):
    try:
        customer = Customer.objects.create(name=name)
        return True, f"\033[92mCustomer '{name}' created successfully.\033[0m"
    except Exception as e:
        return False, f"\033[91mFailed to create customer: {str(e)}\033[0m"

def update_customer(customer_id, **kwargs):
    try:
        customer = Customer.objects.get(id=customer_id)
        for key, value in kwargs.items():
            setattr(customer, key, value)
        customer.save()
        return True, "\033[92mCustomer updated successfully.\033[0m"
    except Customer.DoesNotExist:
        return False, "\033[91mCustomer not found.\033[0m"

def delete_customer(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return True, "\033[92mCustomer deleted successfully\033[0m"
    except Customer.DoesNotExist:
        return False, "\033[91mCustomer does not exist\033[0m"

# CRUD operations for CustomerOrder
def create_customer_order(customer, order_list, created_date, paid):
    try:
        order = CustomerOrder.objects.create(customer=customer, created_date=created_date, paid=paid)
        order.order.set(order_list)
        order.calculate_total_price()
        return True, "\033[92mCustomer order created successfully.\033[0m"
    except Exception as e:
        return False, f"\033[91mFailed to create customer order: {str(e)}\033[0m"

def update_customer_order(order_id, **kwargs):
    try:
        order = CustomerOrder.objects.get(id=order_id)
        for key, value in kwargs.items():
            setattr(order, key, value)
        order.save()
        return True, "\033[92mCustomer order updated successfully\033[0m"
    except CustomerOrder.DoesNotExist:
        return False, "\033[91mCustomer order not found\033[0m"

def delete_customer_order(order_id):
    try:
        order = CustomerOrder.objects.get(id=order_id)
        order.delete()
        return True, "\033[92mCustomer order deleted successfully\033[0m"
    except CustomerOrder.DoesNotExist:
        return False, "\033[91mCustomer order not found\033[0m"

# Display order history for a customer
def display_order_history(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        orders = CustomerOrder.objects.filter(customer=customer)
        print("\033[96m" + f"Order History for Customer: {customer.name}" + "\033[0m")
        for order in orders:
            print(order)
        return True, "\033[92mOrder history displayed successfully\033[0m"
    except Customer.DoesNotExist:
        return False, "\033[91mCustomer not found\033[0m"

# Nest menu options for better user flow
def main_menu():
    print_separator()
    print("\033[96m" + "1. Manage Vehicles" + "\033[0m")
    print_separator()
    print("\033[95m" + "2. Manage Customers" + "\033[0m")
    print_separator()
    print("\033[94m" + "3. Manage Orders" + "\033[0m")
    print_separator()
    print("\033[93m" + "4. Exit" + "\033[0m")
    print_separator()

def vehicle_menu():
    print_separator()
    print("\033[96m" + "Vehicle Menu:" + "\033[0m")
    print_separator()
    print("\033[95m" + "1. Create Vehicle" + "\033[0m")
    print_separator()
    print("\033[94m" + "2. Update Vehicle" + "\033[0m")
    print_separator()
    print("\033[93m" + "3. Delete Vehicle" + "\033[0m")
    print_separator()
    print("\033[92m" + "4. Back to Main Menu" + "\033[0m")
    print_separator()

def customer_menu():
    print_separator()
    print("\033[96m" + "Customer Menu:" + "\033[0m")
    print_separator()
    print("\033[95m" + "1. Create Customer" + "\033[0m")
    print_separator()
    print("\033[94m" + "2. Update Customer" + "\033[0m")
    print_separator()
    print("\033[93m" + "3. Delete Customer" + "\033[0m")
    print_separator()
    print("\033[92m" + "4. Back to Main Menu" + "\033[0m")
    print_separator()

def order_menu():
    print_separator()
    print("\033[96m" + "Order Menu:" + "\033[0m")
    print_separator()
    print("\033[95m" + "1. Create Order" + "\033[0m")
    print_separator()
    print("\033[94m" + "2. Update Order" + "\033[0m")
    print_separator()
    print("\033[93m" + "3. Delete Order" + "\033[0m")
    print_separator()
    print("\033[92m" + "4. Display Order History for a Customer" + "\033[0m")
    print_separator()
    print("\033[91m" + "5. Back to Main Menu" + "\033[0m")
    print_separator()

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("\033[92mEnter your choice: \033[0m")
        if choice == "1":
            while True:
                vehicle_menu()
                vehicle_choice = input("\033[92mEnter your choice: \033[0m")
                if vehicle_choice == "1":
                    type = input("\033[96mEnter vehicle type: \033[0m")
                    number_in_stock = int(input("\033[96mEnter number in stock: \033[0m"))
                    price = float(input("\033[96mEnter price: \033[0m"))
                    color = input("\033[96mEnter color (optional): \033[0m")
                    success, message = create_vehicle(type, number_in_stock, price, color)
                    print(message)
                elif vehicle_choice == "2":
                    vehicle_id = int(input("\033[96mEnter vehicle ID to update: \033[0m"))
                    # Here, you can provide options to update specific fields like type, number_in_stock, price, color, etc.
                    print("\033[96mChoose which fields to update (leave blank to keep current value):\033[0m")
                    new_type = input(f"\033[96mEnter new vehicle type (current: {Vehicle.objects.get(id=vehicle_id).type}): \033[0m") or None
                    new_number_in_stock = input(f"\033[96mEnter new number in stock (current: {Vehicle.objects.get(id=vehicle_id).number_in_stock}): \033[0m") or None
                    new_price = input(f"\033[96mEnter new price (current: {Vehicle.objects.get(id=vehicle_id).price}): \033[0m") or None
                    new_color = input(f"\033[96mEnter new color (current: {Vehicle.objects.get(id=vehicle_id).color}): \033[0m") or None
                    success, message = update_vehicle(vehicle_id, type=new_type, number_in_stock=new_number_in_stock, price=new_price, color=new_color)
                    print(message)
                    if success:
                        print("\033[96mUpdated vehicle information:\033[0m")
                        print(Vehicle.objects.get(id=vehicle_id))
                elif vehicle_choice == "3":
                    vehicle_id = int(input("\033[96mEnter vehicle ID to delete: \033[0m"))
                    success, message = delete_vehicle(vehicle_id)
                    print(message)
                elif vehicle_choice == "4":
                    break
                else:
                    print("\033[91mInvalid choice. Please try again.\033[0m")
        elif choice == "2":
            while True:
                customer_menu()
                customer_choice = input("\033[92mEnter your choice: \033[0m")
                if customer_choice == "1":
                    name = input("\033[96mEnter customer name: \033[0m")
                    success, message = create_customer(name)
                    print(message)
                elif customer_choice == "2":
                    customer_id = int(input("\033[96mEnter customer ID to update: \033[0m"))
                    new_name = input("\033[96mEnter new name: \033[0m")
                    success, message = update_customer(customer_id, name=new_name)
                    print(message)
                    if success:
                        print("\033[96mUpdated customer information:\033[0m")
                        print(Customer.objects.get(id=customer_id))
                elif customer_choice == "3":
                    customer_id = int(input("\033[96mEnter customer ID to delete: \033[0m"))
                    success, message = delete_customer(customer_id)
                    print(message)
                elif customer_choice == "4":
                    break
                else:
                    print("\033[91mInvalid choice. Please try again.\033[0m")
        elif choice == "3":
            while True:
                order_menu()
                order_choice = input("\033[92mEnter your choice: \033[0m")
                if order_choice == "1":
                    # Create a new order
                    customer_id = int(input("\033[96mEnter customer ID: \033[0m"))
                    vehicle_ids = input("\033[96mEnter vehicle IDs (comma-separated): \033[0m").split(',')
                    created_date = input("\033[96mEnter created date (YYYY-MM-DD HH:MM:SS): \033[0m")
                    paid = input("\033[96mIs the order paid? (True/False): \033[0m").lower() == "true"
                    order_list = []
                    for vehicle_id in vehicle_ids:
                        try:
                            order_list.append(Vehicle.objects.get(id=int(vehicle_id)))
                        except Vehicle.DoesNotExist:
                            print(f"\033[91mVehicle with ID {vehicle_id} does not exist.\033[0m")
                    success, message = create_customer_order(customer_id, order_list, created_date, paid)
                    print(message)
                elif order_choice == "2":
                    # Update order details
                    order_id = int(input("\033[96mEnter order ID to update: \033[0m"))
                    new_created_date = input("\033[96mEnter new created date (YYYY-MM-DD HH:MM:SS): \033[0m")
                    new_paid = input("\033[96mIs the order paid? (True/False): \033[0m").lower() == "true"
                    success, message = update_customer_order(order_id, created_date=new_created_date, paid=new_paid)
                    print(message)
                elif order_choice == "3":
                    # Cancel an order
                    order_id = int(input("\033[96mEnter order ID to cancel: \033[0m"))
                    success, message = cancel_customer_order(order_id)
                    print(message)
                elif order_choice == "4":
                    customer_id = int(input("\033[96mEnter customer ID to display order history: \033[0m"))
                    success, message = display_order_history(customer_id)
                    print(message)
                elif order_choice == "5":
                    break
                else:
                    print("\033[91mInvalid choice. Please try again.\033[0m")
        elif choice == "4":
            print("\033[92mExiting program. Goodbye!\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")
            