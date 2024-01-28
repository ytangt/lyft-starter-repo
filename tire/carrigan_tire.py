from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_sensor):
        self.sonsor = tire_wear_sensor
        

    def needs_service(self):
        for i in self.sonsor:
            if i >=0.9:
                return True
        return False
