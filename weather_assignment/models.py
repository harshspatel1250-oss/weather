#Create a class WeatherReading with:

from datetime import datetime

class WeatherReading:
    def __init__(self,station_id,timestamp,temperature,rainfall,humidity):
        self.station_id=station_id
        self.timestamp=timestamp
        self.temperature=float(temperature)
        self.rainfall=float(rainfall)
        self.humidity=float(humidity)
    
#add methods
    def is_hot(self,threshold=40):
        return self.temperature > threshold
    
    def is_heavy_rain(self,threshold=50):
        return self.rainfall > threshold
    