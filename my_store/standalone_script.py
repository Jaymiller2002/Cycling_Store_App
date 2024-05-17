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

# from my_app.models import Vehicle, Customer, CustomerOrder

# # Function to print separator in cyan blue
# def print_separator():
#     print("\033[96m" + "=" * 40 + "\033[0m")  # Cyan blue color


# # ASCII art for a car
# car_art = """🚗"""

# # ASCII art for Manage Customers
# manage_customers_emoji = """👤"""

# #ASCII art for Manage Orders
# manage_orders_emoji = """📦"""

# #ASCII art for back to menu
# back_to_menu_emoji = """⬅️"""

# #ASCII art for EXIT
# exit_art = """❌"""



# # CRUD operations for Vehicle
# def create_vehicle(type, number_in_stock, price, color):
#     try:
#         vehicle = Vehicle.objects.create(type=type, number_in_stock=number_in_stock, price=price, color=color)
#         return True, "Vehicle created successfully."
#     except Exception as e:
#         return False, f"Failed to create vehicle: {str(e)}"
# # **kwarg becomes a dictionary where vehicle, key, and value are the arguemnets
# def update_vehicle(vehicle_id, **kwargs):
#     try:
#         vehicle = Vehicle.objects.get(id=vehicle_id)
#         for key, value in kwargs.items():
#             setattr(vehicle, key, value)
#         vehicle.save()
#         return True, "Vehicle updated successfully."
#     except Vehicle.DoesNotExist:
#         return False, "Vehicle not found."

# def delete_vehicle(vehicle_id):
#     try:
#         vehicle = Vehicle.objects.get(id=vehicle_id)
#         vehicle.delete()
#         return True, "Vehicle deleted successfully"
#     except Vehicle.DoesNotExist:
#         return False, "Vehicle not found"

# # CRUD operations for Customer
# def create_customer(name):
#     try:
#         customer = Customer.objects.create(name=name)
#         return True, f"Customer '{name}' created successfully."
#     except Exception as e:
#         return False, f"Failed to create customer: {str(e)}"

# def update_customer(customer_id, **kwargs):
#     try:
#         customer = Customer.objects.get(id=customer_id)
#         for key, value in kwargs.items():
#             setattr(customer, key, value)
#         customer.save()
#         return True, "Customer updated successfully."
#     except Customer.DoesNotExist:
#         return False, "Customer not found."

# def delete_customer(customer_id):
#     try:
#         customer = Customer.objects.get(id=customer_id)
#         customer.delete()
#         return True, "Customer deleted successfully"
#     except Customer.DoesNotExist:
#         return False, "Customer does not exist"

# # CRUD operations for CustomerOrder
# def create_customer_order(customer, order_list, created_date, paid):
#     try:
#         order = CustomerOrder.objects.create(customer=customer, created_date=created_date, paid=paid)
#         order.order.set(order_list)
#         order.calculate_total_price()
#         return True, "Customer order created successfully."
#     except Exception as e:
#         return False, f"Failed to create customer order: {str(e)}"

# def update_customer_order(order_id, **kwargs):
#     try:
#         order = CustomerOrder.objects.get(id=order_id)
#         for key, value in kwargs.items():
#             setattr(order, key, value)
#         order.save()
#         return True, "Customer order updated successfully"
#     except CustomerOrder.DoesNotExist:
#         return False, "Customer order not found"

# def delete_customer_order(order_id):
#     try:
#         order = CustomerOrder.objects.get(id=order_id)
#         order.delete()
#         return True, "Customer order deleted successfully"
#     except CustomerOrder.DoesNotExist:
#         return False, "Customer order not found"

# # Display order history for a customer
# def display_order_history(customer_id=None):
#     try:
#         if customer_id is not None:
#             # Display order history for a specific customer
#             customer = Customer.objects.get(id=customer_id)
#             orders = CustomerOrder.objects.filter(customer=customer)
#             print(f"Order History for Customer: {customer.name}")
#             for order in orders:
#                 print(order)
#         else:
#             # Display order history for all customers
#             all_orders = CustomerOrder.objects.all()
#             print("Order History for All Customers:")
#             for order in all_orders:
#                 print(order)
#         return True, "Order history displayed successfully"
#     except Customer.DoesNotExist:
#         return False, "Customer not found"

# # Define separator printing function
# def print_separator():
#     print("\033[96m" + "=" * 40 + "\033[0m")  # Cyan blue color

# # Main menu and sub-menus with ASCII art
# def main_menu():
#     print_separator()
#     print("\033[96m" + "1. Manage Vehicles" + "\033[0m")
#     print(car_art)
#     print_separator()
#     print("\033[95m" + "2. Manage Customers" + "\033[0m")
#     print(manage_customers_emoji)
#     print_separator()
#     print("\033[94m" + "3. Manage Orders" + "\033[0m")
#     print(manage_orders_emoji)
#     print_separator()
#     print("\033[93m" + "4. Exit" + "\033[0m")
#     print(exit_art)
#     print_separator()

# def vehicle_menu():
#     print_separator()
#     print("\033[96m" + "Vehicle Menu:" + "\033[0m")
#     print_separator()
#     print("\033[95m" + "1. Create Vehicle" + "\033[0m")
#     print(car_art)
#     print_separator()
#     print("\033[94m" + "2. Update Vehicle" + "\033[0m")
#     print(car_art)
#     print_separator()
#     print("\033[93m" + "3. Delete Vehicle" + "\033[0m")
#     print(car_art)
#     print_separator()
#     print("\033[92m" + "4. Back to Main Menu" + "\033[0m")
#     print(back_to_menu_emoji)
#     print_separator()

# def customer_menu():
#     print_separator()
#     print("\033[96m" + "Customer Menu:" + "\033[0m")
#     print_separator()
#     print("\033[95m" + "1. Create Customer" + "\033[0m")
#     print(manage_customers_emoji)
#     print_separator()
#     print("\033[94m" + "2. Update Customer" + "\033[0m")
#     print(manage_customers_emoji)
#     print_separator()
#     print("\033[93m" + "3. Delete Customer" + "\033[0m")
#     print(manage_customers_emoji)
#     print_separator()
#     print("\033[92m" + "4. Back to Main Menu" + "\033[0m")
#     print(back_to_menu_emoji)
#     print_separator()

# def order_menu():
#     print_separator()
#     print("\033[96m" + "Order Menu:" + "\033[0m")
#     print_separator()
#     print("\033[95m" + "1. Create Order" + "\033[0m")
#     print(manage_orders_emoji)
#     print_separator()
#     print("\033[94m" + "2. Update Order" + "\033[0m")
#     print(manage_orders_emoji)
#     print_separator()
#     print("\033[93m" + "3. Delete Order" + "\033[0m")
#     print(manage_orders_emoji)
#     print_separator()
#     print("\033[92m" + "4. Display Order History for a Customer" + "\033[0m")
#     print(manage_orders_emoji)
#     print_separator()
#     print("\033[91m" + "5. Back to Main Menu" + "\033[0m")
#     print(back_to_menu_emoji)
#     print_separator()

# if __name__ == "__main__":
#     while True:
#         main_menu()
#         choice = input("\033[92mEnter your choice: \033[0m")
#         if choice == "1":
#             while True:
#                 vehicle_menu()
#                 vehicle_choice = input("\033[92mEnter your choice: \033[0m")
#                 if vehicle_choice == "1":
#                     type = input("\033[96mEnter vehicle type: \033[0m")
#                     number_in_stock = int(input("\033[96mEnter number in stock: \033[0m"))
#                     price = float(input("\033[96mEnter price: \033[0m"))
#                     color = input("\033[96mEnter color (optional): \033[0m")
#                     success, message = create_vehicle(type, number_in_stock, price, color)
#                     print(message)
#                 elif vehicle_choice == "2":
#                     vehicle_id = int(input("\033[96mEnter vehicle ID to update: \033[0m"))
#                     # Here, you can provide options to update specific fields like type, number_in_stock, price, color, etc.
#                     print("\033[96mChoose which fields to update (leave blank to keep current value):\033[0m")
#                     new_type = input(f"\033[96mEnter new vehicle type (current: {Vehicle.objects.get(id=vehicle_id).type}): \033[0m") or None
#                     new_number_in_stock = input(f"\033[96mEnter new number in stock (current: {Vehicle.objects.get(id=vehicle_id).number_in_stock}): \033[0m") or None
#                     new_price = input(f"\033[96mEnter new price (current: {Vehicle.objects.get(id=vehicle_id).price}): \033[0m") or None
#                     new_color = input(f"\033[96mEnter new color (current: {Vehicle.objects.get(id=vehicle_id).color}): \033[0m") or None
#                     success, message = update_vehicle(vehicle_id, type=new_type, number_in_stock=new_number_in_stock, price=new_price, color=new_color)
#                     print(message)
#                     if success:
#                         print("\033[96mUpdated vehicle information:\033[0m")
#                         print(Vehicle.objects.get(id=vehicle_id))
#                 elif vehicle_choice == "3":
#                     vehicle_id = int(input("\033[96mEnter vehicle ID to delete: \033[0m"))
#                     success, message = delete_vehicle(vehicle_id)
#                     print(message)
#                 elif vehicle_choice == "4":
#                     break
#                 else:
#                     print("\033[91mInvalid choice. Please try again.\033[0m")
#         elif choice == "2":
#             while True:
#                 customer_menu()
#                 customer_choice = input("\033[92mEnter your choice: \033[0m")
#                 if customer_choice == "1":
#                     name = input("\033[96mEnter customer name: \033[0m")
#                     success, message = create_customer(name)
#                     print(message)
#                 elif customer_choice == "2":
#                     customer_id = int(input("\033[96mEnter customer ID to update: \033[0m"))
#                     new_name = input("\033[96mEnter new name: \033[0m")
#                     success, message = update_customer(customer_id, name=new_name)
#                     print(message)
#                     if success:
#                         print("\033[96mUpdated customer information:\033[0m")
#                         print(Customer.objects.get(id=customer_id))
#                 elif customer_choice == "3":
#                     customer_id = int(input("\033[96mEnter customer ID to delete: \033[0m"))
#                     success, message = delete_customer(customer_id)
#                     print(message)
#                 elif customer_choice == "4":
#                     break
#                 else:
#                     print("\033[91mInvalid choice. Please try again.\033[0m")
#         elif choice == "3":
#             while True:
#                 order_menu()
#                 order_choice = input("\033[92mEnter your choice: \033[0m")
#                 if order_choice == "1":
#                     # Create a new order
#                     customer_id = int(input("\033[96mEnter customer ID: \033[0m"))
#                     vehicle_ids = input("\033[96mEnter vehicle IDs (comma-separated): \033[0m").split(',')
#                     created_date = input("\033[96mEnter created date (YYYY-MM-DD HH:MM:SS): \033[0m")
#                     paid = input("\033[96mIs the order paid? (True/False): \033[0m").lower() == "true"
#                     order_list = []
#                     for vehicle_id in vehicle_ids:
#                         try:
#                             order_list.append(Vehicle.objects.get(id=int(vehicle_id)))
#                         except Vehicle.DoesNotExist:
#                             print(f"\033[91mVehicle with ID {vehicle_id} does not exist.\033[0m")
#                     success, message = create_customer_order(customer_id, order_list, created_date, paid)
#                     print(message)
#                 elif order_choice == "2":
#                     # Update order details
#                     order_id = int(input("\033[96mEnter order ID to update: \033[0m"))
#                     new_created_date = input("\033[96mEnter new created date (YYYY-MM-DD HH:MM:SS): \033[0m")
#                     new_paid = input("\033[96mIs the order paid? (True/False): \033[0m").lower() == "true"
#                     success, message = update_customer_order(order_id, created_date=new_created_date, paid=new_paid)
#                     print(message)
#                 elif order_choice == "3":
#                     # Cancel an order
#                     order_id = int(input("\033[96mEnter order ID to cancel: \033[0m"))
#                     success, message = delete_customer_order(order_id)
#                     print(message)
#                 elif order_choice == "4":
#                     customer_id_input = input("\033[96mEnter customer ID to display order history (leave blank to show all): \033[0m")
#                     if customer_id_input:
#                         customer_id = int(customer_id_input)
#                         success, message = display_order_history(customer_id)
#                     else:
#                         success, message = display_order_history()
#                     print(message)
#                 elif order_choice == "5":
#                     break
#                 else:
#                     print("\033[91mInvalid choice. Please try again.\033[0m")
#         elif choice == "4":
#             print("\033[92mExiting program. Goodbye! 👋\033[0m")
#             break
#         else:
#             print("\033[91mInvalid choice. Please try again.\033[0m")



from django.core.management.base import BaseCommand
from my_app.models import Vehicle, Customer, CustomerOrder, OrderItem

class Command(BaseCommand):
    help = 'Manage the cycling store'

    def handle(self, *args, **kwargs):
        self.clear_database()
        self.main_menu()

    def clear_database(self):
        Vehicle.objects.all().delete()
        Customer.objects.all().delete()
        CustomerOrder.objects.all().delete()
        OrderItem.objects.all().delete()

    def main_menu(self):
        while True:
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


if __name__ == "__main__":
    command = Command()
    command.handle()


