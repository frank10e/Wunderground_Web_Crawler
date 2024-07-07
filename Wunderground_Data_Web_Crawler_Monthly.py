import datetime
import requests,csv
from collections import defaultdict


headers = {
    "authority": "api.weather.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.wunderground.com",
    "pragma": "no-cache",
    "referer": "https://www.wunderground.com/",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^104^^, ^\\^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

def get_result():
    with open('weather_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Max Temp", "Min Temp", "Avg Temp",
                         "Max Dew Point", "Min Dew Point", "Avg Dew Point",
                         "Max Humidity", "Min Humidity", "Avg Humidity",
                         "Max Pressure", "Min Pressure", "Avg Pressure",
                         "Max Wind Speed", "Min Wind Speed", "Avg Wind Speed",
                         "Total Precipitation"])

        dates = get_month_start_end_dates()
        for start, end in dates:
            print(f"--------------------Acquiring Data：{start}-{end}--------------------------")

            url = "https://api.weather.com/v1/location/KTUS:9:US/observations/historical.json"
            params = {
                "apiKey": "e1f10a1e78da46f5b10a1e78da96f525",
                "units": "e",
                "startDate": start,
                "endDate": end
            }
            headers = {}  # For adding necessary headers
            response = requests.get(url, headers=headers, params=params)
            print(response.status_code)
            if response.status_code != 200:
                print(f"Denied：{response.status_code}")
                continue

            res = response.json()
            print(res)
            data_list = res.get("observations", [])

            if len(data_list) > 0:
                daily_data = defaultdict(lambda: defaultdict(list))

                for aa in data_list:
                    expire_time_gmt = aa["expire_time_gmt"]
                    expire_time = convert_negative_timestamp(expire_time_gmt)
                    print(expire_time)
                    date = expire_time.split(' ')[0]

                    temp = aa.get("temp")
                    dewPt = aa.get("dewPt")
                    rh = aa.get("rh")
                    pressure = aa.get("pressure")
                    wspd = aa.get("wspd")
                    precip_total = aa.get("precip_total")

                    if temp is not None:
                        daily_data[date]['temp'].append(temp)
                    if dewPt is not None:
                        daily_data[date]['dewPt'].append(dewPt)
                    if rh is not None:
                        daily_data[date]['rh'].append(rh)
                    if pressure is not None:
                        daily_data[date]['pressure'].append(pressure)
                    if wspd is not None:
                        daily_data[date]['wspd'].append(wspd)
                    if precip_total is not None:
                        daily_data[date]['precip_total'].append(precip_total)

                for date, metrics in daily_data.items():
                    if metrics['temp']:
                        max_temp = max(metrics['temp'])
                        min_temp = min(metrics['temp'])
                        avg_temp = sum(metrics['temp']) / len(metrics['temp'])
                    else:
                        max_temp = min_temp = avg_temp = None

                    if metrics['dewPt']:
                        max_dewPt = max(metrics['dewPt'])
                        min_dewPt = min(metrics['dewPt'])
                        avg_dewPt = sum(metrics['dewPt']) / len(metrics['dewPt'])
                    else:
                        max_dewPt = min_dewPt = avg_dewPt = None

                    if metrics['rh']:
                        max_rh = max(metrics['rh'])
                        min_rh = min(metrics['rh'])
                        avg_rh = sum(metrics['rh']) / len(metrics['rh'])
                    else:
                        max_rh = min_rh = avg_rh = None

                    if metrics['pressure']:
                        max_pressure = max(metrics['pressure'])
                        min_pressure = min(metrics['pressure'])
                        avg_pressure = sum(metrics['pressure']) / len(metrics['pressure'])
                    else:
                        max_pressure = min_pressure = avg_pressure = None

                    if metrics['wspd']:
                        max_wspd = max(metrics['wspd'])
                        min_wspd = min(metrics['wspd'])
                        avg_wspd = sum(metrics['wspd']) / len(metrics['wspd'])
                    else:
                        max_wspd = min_wspd = avg_wspd = None

                    total_precip = sum(metrics['precip_total']) if metrics['precip_total'] else 0

                    writer.writerow([date, max_temp, min_temp, avg_temp,
                                     max_dewPt, min_dewPt, avg_dewPt,
                                     max_rh, min_rh, avg_rh,
                                     max_pressure, min_pressure, avg_pressure,
                                     max_wspd, min_wspd, avg_wspd,
                                     total_precip])
                print(f'Data Saved to csv file')
            else:
                print(f'No Data')
                break






import datetime
import pytz


def convert_time(timestamp):
    # convert the timestamp to a datetime object
    timestamp = int(timestamp)
    if len(str(timestamp)) == 13:
        timestamp /= 1000

    # convert the timestamp to a datetime object 
    dt_utc = datetime.datetime.fromtimestamp(timestamp, tz=pytz.utc)

    # convert the datetime object to Arizona time 
    arizona = pytz.timezone("US/Arizona")
    dt_arizona = dt_utc.astimezone(arizona)

    # format the date
    output_format = "%Y-%m-%d %H:%M:%S"
    formatted_date = dt_arizona.strftime(output_format)

    return formatted_date

def convert_negative_timestamp(timestamp):
    # calculate the base time from 1970-01-01
    base_time = datetime.datetime(1970, 1, 1)
    offset = datetime.timedelta(seconds=abs(timestamp))

    # calculate the final time
    if timestamp < 0:
        final_time = base_time - offset
    else:
        final_time = base_time + offset
    final_time -= datetime.timedelta(hours=9)
        # transfer to Arizona time
    output_format = "%Y-%m-%d %H:%M:%S"
    formatted_date = final_time.strftime(output_format)

    return formatted_date

    # return final_time

def get_month_start_end_dates(start_year=1949):
    current_year = datetime.datetime.now().year
    dates = []

    for year in range(start_year, current_year + 1):
        for month in range(1, 13):
            first_day = datetime.date(year, month, 1)
            if month == 12:
                last_day = datetime.date(year, month, 31)
            else:
                last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            dates.append((first_day.strftime('%Y%m%d'), last_day.strftime('%Y%m%d')))

    return dates

if __name__ == '__main__':
    get_result()