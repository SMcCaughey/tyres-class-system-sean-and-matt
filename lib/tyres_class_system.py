import datetime as dt

class Car():
    def __init__(self):
        self.RF = Tyre()
        self.LF = Tyre()
        self.RR = Tyre()
        self.LR = Tyre()

    def retrieve_single_tyre_data(self,tyre_ref):
        if tyre_ref == "RF":
            if self.RF.data == []:
                return "No data recorded"
            return self.RF.data
        if tyre_ref == "LF":
            if self.RF.data == []:
                return "No data recorded"
            return self.LF.data
        if tyre_ref == "RR":
            if self.RF.data == []:
                return "No data recorded"
            return self.RR.data
        if tyre_ref == "LR":
            if self.RF.data == []:
                return "No data recorded"
            return self.LR.data
        return "Not a valid tyre"
    
    def retrieve_overview_data(self):
        RF_string = ""
        if self.RF.data == []:
            RF_string = "RF: No recorded data"
        else: 
            RF_data = self.RF.data[-1] # {date_of_reading: [pressure, depth]}
            date_of_reading = list(RF_data.keys())[0]
            RF_string = f"RF: Pressure {RF_data[date_of_reading][0]}, Depth {RF_data[date_of_reading][1]}, recorded on {date_of_reading}"

        LF_string = ""
        if self.LF.data == []:
            LF_string = "LF: No recorded data"
        else:
            LF_data = self.LF.data[-1]
            date_of_reading = list(LF_data.keys())[0]
            pressure_reading = LF_data[date_of_reading][0]
            depth_reading = LF_data[date_of_reading][1]
            LF_string = f"LF: Pressure {pressure_reading}, Depth {depth_reading}, recorded on {date_of_reading}"
        # RR_data = self.RR.data[-1]
        # date_of_reading = list(RR_data.keys())[0]
        # pressure_reading = RR_data[date_of_reading][0]
        # depth_reading = RR_data[date_of_reading][1]
        # LR_data = self.LR.data[-1]
        # date_of_reading = list(LR_data.keys())[0]
        # pressure_reading = LR_data[date_of_reading][0]
        # depth_reading = LR_data[date_of_reading][1]
        return f"{RF_string}, {LF_string}"
        

class Tyre():
    def __init__(self):
        self.data = []
    
    def record_data(self, pressure, depth, date):
        self.data.append({date: [pressure, depth]})
        print(self.data)