import json
from processor import (
    load_weather_data,
    get_daily_avg_temperature,
    get_daily_rainfall
)
from alerts import generate_alerts

def main():
    readings = load_weather_data("weather_data.json")

    avg_temp = get_daily_avg_temperature(readings)
    rainfall = get_daily_rainfall(readings)
    alerts = generate_alerts(readings)

    summary = {"daily_summary": {}}

    for station in avg_temp:
        summary["daily_summary"][station] = {}
        for date in avg_temp[station]:
            summary["daily_summary"][station][date] = {
                "avg_temperature": avg_temp[station][date],
                "total_rainfall": rainfall.get(station, {}).get(date, 0),
                "alerts": alerts.get(station, {}).get(date, [])
            }

    file = open("summary.json", "w")
    json.dump(summary, file, indent=4)
    file.close()

    print("Weather summary generated successfully.")

if __name__ == "__main__":
    main()
