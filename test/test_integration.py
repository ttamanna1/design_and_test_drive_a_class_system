from lib.tyre import Tyre
from lib.car import Car

"""
add tyre to car

"""
def test_add_tyre_to_car():
    car = Car()
    car.add_tyre('FL')
    assert car.list_tyre() == {'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}