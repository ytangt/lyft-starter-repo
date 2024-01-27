
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine



class CarFactory:

    @staticmethod
    def create_callope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine, battery)
        

    @staticmethod
    def  create_Glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        Car = Car(engine, battery)
        

    @staticmethod
    def  create_Palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date,current_date)
        Car = Car(engine, battery)
        
   
    @staticmethod
    def  create_Rorschan(current_date, last_service_date, warning_light_is_on):
        engine = WilloughbyEngine(warning_light_is_on)
        battery = NubbinBattery(last_service_date,current_date)
        Car = Car(engine, battery)

    @staticmethod
    def  create_Thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        Car = Car(engine, battery)