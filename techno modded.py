from abc import ABC, abstractmethod

# Define Product Interfaces
class Device(ABC):
    @abstractmethod
    def assemble(self, specifications):
        pass

# Implement Concrete Products
class Smartphone(Device):
    def assemble(self, specifications):
        print("Assembling Smartphone with specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")

class Camera(Device):
    def assemble(self, specifications):
        print("Assembling Camera with specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")

class Laptop(Device):
    def assemble(self, specifications):
        print("Assembling Laptop with specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")

class Desktop(Device):
    def assemble(self, specifications):
        print("Assembling Desktop with specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")

class Monitor(Device):
    def assemble(self, specifications):
        print("Assembling Monitor with specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")

# Define Factory Interface
class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self):
        pass

# Implement Concrete Factories
class SmartphoneFactory(DeviceFactory):
    def create_device(self):
        return Smartphone()

class CameraFactory(DeviceFactory):
    def create_device(self):
        return Camera()

class LaptopFactory(DeviceFactory):
    def create_device(self):
        return Laptop()

class DesktopFactory(DeviceFactory):
    def create_device(self):
        return Desktop()

class MonitorFactory(DeviceFactory):
    def create_device(self):
        return Monitor()

# Client Code
def order_device(factory, cart):
    device = factory.create_device()
    specifications = {}
    # Gather specifications from the user
    if isinstance(device, Smartphone):
        specifications['model'] = input("Enter smartphone model: ")
        specifications['RAM'] = input("Enter RAM capacity: ")
        specifications['storage'] = input("Enter storage capacity: ")
    elif isinstance(device, Camera):
        specifications['model'] = input("Enter camera model: ")
        specifications['image_sensor'] = input("Enter camera image sensor type: ")
        specifications['resolution'] = input("Enter camera resolution: ")
        specifications['zoom'] = input("Enter camera zoom level: ")
        specifications['body_type'] = input("Enter camera body type (mirrorless, slr, dslr, digital): ")
    elif isinstance(device, Laptop) or isinstance(device, Desktop):
        specifications['model'] = input("Enter {} model: ".format("laptop" if isinstance(device, Laptop) else "desktop"))
        specifications['processor'] = input("Enter processor type: ")
        specifications['RAM'] = input("Enter RAM capacity: ")
        specifications['storage'] = input("Enter storage capacity: ")
        if isinstance(device, Desktop):
            specifications['motherboard'] = input("Enter motherboard type: ")
            specifications['gpu'] = input("Enter GPU type: ")
            specifications['psu'] = input("Enter PSU wattage: ")
    elif isinstance(device, Monitor):
        specifications['model'] = input("Enter monitor model: ")
        specifications['size'] = input("Enter monitor size: ")
        specifications['resolution'] = input("Enter monitor resolution: ")
        specifications['refresh_rate'] = input("Enter monitor refresh rate (Hz): ")

    device.assemble(specifications)
    cart.append((device.__class__.__name__, specifications))

def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item[0]}:")
            for key, value in item[1].items():
                print(f"   - {key}: {value}")
            print()

def checkout(cart):
    if not cart:
        print("\nYour cart is empty. Please add items before checking out.")
    else:
        print("\nYour Purchased Items:")
        for item in cart:
            print(f"{item[0]}:")
            for key, value in item[1].items():
                print(f"   - {key}: {value}")
            print()
        cart.clear()


def welcome_message():
    print("Welcome to Techno71 Gadget Factory!!!")

def show_menu():
    print("\nSelect an option:")
    print("1. Buy gadget")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

# Example usage
if __name__ == "__main__":
    welcome_message()
    cart = []

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nSelect the device you want to order:")
            print("1. Smartphone")
            print("2. Camera")
            print("3. Laptop")
            print("4. Desktop")
            print("5. Monitor")
            
            device_choice = int(input("Enter your choice: "))

            # Select appropriate factory based on user's choice
            if device_choice == 1:
                selected_factory = SmartphoneFactory()
            elif device_choice == 2:
                selected_factory = CameraFactory()
            elif device_choice == 3:
                selected_factory = LaptopFactory()
            elif device_choice == 4:
                selected_factory = DesktopFactory()
            elif device_choice == 5:
                selected_factory = MonitorFactory()
            else:
                print("Invalid choice!")
                continue

            # Place an order for the desired device
            order_device(selected_factory, cart)
        elif choice == 2:
            display_cart(cart)
        elif choice == 3:
            checkout(cart)
        elif choice == 4:
            print("\nThank you for visiting Techno71 Gadget Factory!")
            break
        else:
            print("\nInvalid choice! Please select again.")
