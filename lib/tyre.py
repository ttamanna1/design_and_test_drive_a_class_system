
class Tyre:

    def __init__(self, position):
        # Parameters:
        #   position
        self.position = position
        self.readings = []

    def add_readings(self, pressure, tread_depth, date):
        self.readings.append({'pressure': pressure, 'tread depth': tread_depth, 'date': date})

    def list_all_readings(self):
        # Returns:
        # {}
        return self.readings

    def list_current_reading(self):
        # Returns:
        # {}
        return [self.readings[-1]]