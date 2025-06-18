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


"""
listing all readings of tyre

"""
def test_list_all_readings_of_tyre():
    tyre = Tyre('FL')
    tyre.add_readings(250, 8, '17/06/25')
    tyre.add_readings(300, 9, '16/05/25')
    assert tyre.list_all_readings() == [
        {'pressure': 250, 'tread depth': 8, 'date': '17/06/25'},
        {'pressure': 300, 'tread depth': 9, 'date': '16/05/25'}
    ]

"""
listing current reading of tyre

"""
def test_current_reading_of_tyre():
    tyre = Tyre('FL')
    tyre.add_readings(250, 8, '16/05/25')
    tyre.add_readings(300, 9, '17/06/25')
    assert tyre.list_current_reading() == [
        {'pressure': 300, 'tread depth': 9, 'date': '17/06/25'}
    ]

"""
listing all readings of tyre with no readings

"""
def test_list_no_readings_of_tyre():
    tyre = Tyre('FL')
    assert tyre.list_all_readings() == []