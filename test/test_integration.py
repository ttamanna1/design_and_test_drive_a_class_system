from lib.tyre import Tyre
from lib.car import Car
import pytest

"""
add tyre to car

"""
def test_add_tyre_to_car():
    car = Car()
    car.add_tyre('FL')
    car.tyres['FL'].add_readings(250, 8, '17/06/25')
    assert car.list_tyre() == [{
        'position': 'FL',
        'readings': [{'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}]
    }]
    
def test_adding_same_tyre_to_car_to_raise_exception():
    car = Car()
    car.add_tyre('FL')
    with pytest.raises(Exception) as e:
        car.add_tyre('FL')
    assert str(e.value) == 'FL tyre already added to car'

def test_add_multiple_tyres_to_car():
    car = Car()
    car.add_tyre('FL')
    car.tyres['FL'].add_readings(250, 8, '17/06/25')
    car.add_tyre('FR')
    car.tyres['FR'].add_readings(260, 8, '18/06/25')
    assert car.list_tyre() == [
        {
            'position': 'FL', 
            'readings': [{'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}]
        }, 
        {
            'position': 'FR', 
            'readings': [{'pressure': 260, 'tread depth': 8, 'date': '18/06/25'}]
        }
    ]
