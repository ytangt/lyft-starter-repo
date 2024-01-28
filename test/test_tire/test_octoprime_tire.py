import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.1,0.1,0.9,0.1]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1,0.2,0.2,0.2]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())
