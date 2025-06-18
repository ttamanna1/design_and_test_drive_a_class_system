class Car:

    def __init__(self):
        self.tyres = {}

    def add_tyre(self, position):
        # Parameters:
        #   position: an instance of tyre position as parameter
        #
        # self.tyre[position] = Tyre(position)
        tyre = Tyre(position)
        self.tyres[position] = tyre

        
        # readings_dict = {'pressure': tyre.readings[0], 'tread depth': tyre.readings[1], 'date': tyre.readings[2]}
        # print(readings_dict)

    def list_tyre(self):
        # Returns:
        # A list of tyre readings: pressure, tread depth and date
        #position
        tyre_list =[]
        print(tyre)
        for position, tyre in self.tyres.items():
            
        #   => [{
                # 'pressure': pressure
                # 'tread_depth': tread_depth
                # 'date': date
                # }]
        