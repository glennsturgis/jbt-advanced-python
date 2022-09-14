import time


class Car:
    def __init__(self, name, consumption, tank_size):
        self.name = name
        self.parked = False
        self.fuel = 0
        self.consumption = consumption
        self.mileage = 0
        self.tank_size = tank_size

    def distance_to_fuel(self, distance):
        return distance // self.consumption

    def drive(self, distance):
        time.sleep(1)
        if self.fuel - self.distance_to_fuel(distance) < 0:
            self.mileage += self.fuel * self.consumption
            self.fuel = 0
        else:
            self.fuel -= self.distance_to_fuel(distance)
            self.mileage += distance

    def add_fuel(self, fuel):
        assert fuel >= 0, 'Fuel should be positive'
        if self.fuel + fuel > self.tank_size:
            self.fuel = self.tank_size
        else:
            self.fuel += fuel
