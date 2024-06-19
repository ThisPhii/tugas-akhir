from car import Car
from motorcycle import Motorcycle

def print_vehicle_info(vehicle):
    print(vehicle.get_info())
    vehicle.start_engine()
    vehicle.stop_engine()

def main():
    car = Car("Toyota", "Corolla")
    motorcycle = motorcycle("Yamaha", "MT-07")

    print("Car info:")
    print_vehicle_info(car)

    print("\nMotorcycle info:")
    print_vehicle_info(motorcycle)

if __name__ == "__main__":
    main()
