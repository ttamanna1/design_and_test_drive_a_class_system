# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

Nouns: Record, Tyres, Car, Position, Data, Pressure, Tread Depth, Readings
Verbs: Keep a record, keep track, record, see the details, list.

Noun/verb combos: 
    -Keep a record of car details
    -Keep track of tyres individually
    -Keep track of tyres by position on car
    -Keep a record of tyre pressure
    -Keep a record of tyre tread depth
    -List the tyre's position
    -List readings
    -List when readings are taken

Classes:
-Car:
    -Keep a record of car details
    -Keep track of tyres by position on car
    -List the tyre's position
    -List when readings are taken
-Tyre:
    -Keep track of tyres individually
    -Keep a record of tyre pressure
    -Keep a record of tyre tread depth
    -List the tyre's position
    



## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car(self)             │
│                            │
│ - add_tyre(self, position)                  │
│ - list_tyre(self)               │
           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Tyre(self,position)    │
│                         │
│ - add_readings(self, pressure, tread_depth, date)               │
│ - list_all_readings(self)                │
│ - list_current_reading(self)
  -
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:

    def __init__(self):
        pass # No code here yet

    def add_tyre(self, position):
        # Parameters:
        #   position: an instance of tyre position as parameter
        pass # No code here yet

    def list_tyre(self):
        # Returns:
        # A list of tyre readings: pressure, tread depth and date
        #   => [{
                'pressure': pressure
                'tread_depth': tread_depth
                'date': date
                }]
        pass # No code here yet


class Tyre:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, position):
        # Parameters:
        #   position
        pass # No code here yet

    def add_readings(self, pressure, tread_depth, date):
        pass # No code here yet

    def list_all_readings(self):
        # Returns:
        # {}
        pass

    def list_current_reading(self):
        # Returns:
        # {}
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
add tyre to car

"""
def test_add_tyre_to_car()
    car = Car()
    car.add_tyre('FL')
    assert car.list_tyre() == {'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}

def test_adding_same_tyre_to_car_to_raise_exception()
    car = Car()
    car.add_tyre('FL')
    with pytest.raises(Exception) as e:
        car.add_tyre('FL')
    assert str(e.value) == 'FL tyre already added to car'

def test_add_multiple_tyres_to_car()
    car = Car()
    car.add_tyre('FL')
    car.add_tyre('FR')
    assert car.list_tyre() == [
        {'position': 'FL','pressure': 250, 'tread depth': 8, 'date': '17/06/25'}
        {'position': 'FR','pressure': 250, 'tread depth': 8, 'date': '17/06/25'}

    ]



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

# TYRE TESTS

"""
Instantiated a tyre with a position

"""
tyre = Tyre('FL')
assert tyre.position == 'FL'


"""
add readings to tyre

"""
def test_add_reading_to_tyre()
    tyre = Tyre('FL')
    tyre.add_reading(250, 8, '17/06/25')
    assert tyre.list_current_reading() == {'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}

"""
add readings to tyre with invalid date
raise exception is date is not in datetime object

"""
def test_add_reading_to_tyre_with_invalid_date()
    tyre = Tyre('FL')
    with pytest.raises(Exception) as e:
        tyre.add_reading(250, 8, '1700625')
    assert str(e.value) == "Enter date in correct format"

"""
listing all readings of tyre

"""
def test_list_all_readings_of_tyre()
    tyre = Tyre('FL')
    tyre.add_reading(250, 8, '17/06/25')
    tyre.add_reading(300, 9, '16/05/25')
    assert tyre.list_all_readings_of_tyre() == [
        {'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}
        {'pressure': 300, 'tread depth': 9, 'date': '16/05/25'}
    ]

"""
listing all readings of tyre with no readings

"""
def test_list_no_readings_of_tyre()
    tyre = Tyre('FL')
    assert tyre.list_all_readings_of_tyre() == []


"""
listing current reading of tyre

"""
def test_current_reading_of_tyre()
    tyre = Tyre('FL')
    tyre.add_reading(250, 8, '16/05/25')
    tyre.add_reading(300, 9, '17/06/25')
    assert tyre.list_current_reading_of_tyre() == [
        {'pressure': 300, 'tread depth': 9, 'date': '17/06/25'}
    ]

# CAR TESTS

"""
Instantiated a car with an empty list/dictionary for tyres

"""
car = Car()
assert car.tyres == [] / {}




_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
