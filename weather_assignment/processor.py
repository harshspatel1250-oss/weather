#Load & Validate Data

import json
import logging
from datetime import datetime
from models import WeatherReading

# Error logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

def load_weather_data(filename):
    readings = []

    try:
        file = open(filename, "r")
        data = json.load(file)
        file.close()
    except Exception as e:
        logging.error(f"File read error: {e}")
        return readings

    for record in data:
        try:
            reading = WeatherReading(
                record["station_id"],
                datetime.fromisoformat(record["timestamp"]),
                float(record["temperature"]),
                float(record["rainfall"]),
                float(record["humidity"])
            )
            readings.append(reading)
        except Exception as e:
            logging.error(f"Invalid record skipped: {record}")

    return readings

#Daily Aggregations

def get_daily_avg_temperature(readings):
    result = {}

    for r in readings:
        date = r.timestamp.date().isoformat()
        result.setdefault(r.station_id, {}).setdefault(date, []).append(r.temperature)

    avg_temp = {}
    for station in result:
        avg_temp[station] = {}
        for date in result[station]:
            temps = result[station][date]
            avg_temp[station][date] = round(sum(temps) / len(temps), 2)

    return avg_temp


def get_daily_rainfall(readings):
    rainfall = {}

    for r in readings:
        date = r.timestamp.date().isoformat()
        rainfall.setdefault(r.station_id, {}).setdefault(date, 0)
        rainfall[r.station_id][date] += r.rainfall

    return rainfall
