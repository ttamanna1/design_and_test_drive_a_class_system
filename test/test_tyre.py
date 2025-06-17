from lib.tyre import Tyre

"""
Instantiated a tyre with a position

"""
def test_instatiate_tyre():
    tyre = Tyre('FL')
    assert tyre.position == 'FL'


"""
add readings to tyre

"""
def test_add_reading_to_tyre():
    tyre = Tyre('FL')
    tyre.add_readings(250, 8, '17/06/25')
    assert tyre.list_current_reading() == [{'pressure': 250, 'tread depth': 8, 'date': '17/06/25'}]
