
class Tyre:
    # User-facing properties:
    #   title: string
    #   artist: string

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
        pass

    def list_current_reading(self):
        # Returns:
        # {}
        return self.readings