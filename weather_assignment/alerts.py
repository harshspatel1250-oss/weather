'''Heat Alert → if any reading in a day exceeds 40°C
Heavy Rain Alert → if total daily rainfall > 100 mm'''


def generate_alerts(readings):
    alerts = {}
    daily_rainfall = {}

    for r in readings:
        date = r.timestamp.date().isoformat()

        alerts.setdefault(r.station_id, {}).setdefault(date, [])
        daily_rainfall.setdefault(r.station_id, {}).setdefault(date, 0)

        if r.is_hot() and "HEAT_ALERT" not in alerts[r.station_id][date]:
            alerts[r.station_id][date].append("HEAT_ALERT")

        daily_rainfall[r.station_id][date] += r.rainfall

    for station in daily_rainfall:
        for date in daily_rainfall[station]:
            if daily_rainfall[station][date] > 100:
                alerts[station][date].append("HEAVY_RAIN_ALERT")

    return alerts
