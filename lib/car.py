from lib.tyre import Tyre
class Car:
    def __init__(self):
        self.tyres = {}

    def add_tyre(self, position):
        if position in self.tyres:
            raise Exception(f"{position} tyre already added to car")
        self.tyres[position] = Tyre(position)

    def list_tyre(self):
        tyre_list =[]
        for position, tyre in self.tyres.items():
            readings = tyre.list_current_reading()
            tyre_list.append({
                'position': position,
                'readings': readings
            })
        return tyre_list
        