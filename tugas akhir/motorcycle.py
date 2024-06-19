from vehicle import vehicle

class Motorcycle(vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model}'s engine has stopped.")

    def get_info(self):
        return f"Motorcycle: {self.brand} {self.model}"
