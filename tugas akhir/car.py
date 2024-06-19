from vehicle import vehicle

class Car(vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model}'s engine has stopped.")

    def get_info(self):
        return f"Car: {self.brand} {self.model}"
