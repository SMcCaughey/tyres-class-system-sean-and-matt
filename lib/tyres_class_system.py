import datetime as dt

class Car():
    

class Tyre():
    def __init__(self):
        self.data = []
    
    def record_data(self, pressure, depth, date):
        self.data.append({date: [pressure, depth]})
        print(self.data)