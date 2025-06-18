from lib.car import Car

"""
Instantiated a car with an empty list/dictionary for tyres

"""
def test_instantiate_car():
    car = Car()
    assert car.tyres == {}
    

