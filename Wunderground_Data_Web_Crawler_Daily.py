# https://www.wunderground.com/history/monthly/us/az/tucson/KTUS/date/1960-1
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
    with open('weather_data_daily.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Temperature", "Dew Point", "Humidity",
                         "Wind", "Wind Speed", "Wind Gust",
                         "Pressure", "Precip.", "Condition",
                        ])

        dates = get_month_start_end_dates()
        for start, end in dates:
            print(f"--------------------Get Data：{start}-{end}--------------------------")

            url = "https://api.weather.com/v1/location/KTUS:9:US/observations/historical.json"
            params = {
                "apiKey": "e1f10a1e78da46f5b10a1e78da96f525",
                "units": "e",
                "startDate": start,
                "endDate": end
            }
            headers = {}  
            response = requests.get(url, headers=headers, params=params)
            print(response.status_code)
            if response.status_code == 400:
                print(f"There is no data for this date")
                break

            res = response.json()
            print(res)
            data_list = res.get("observations", [])

            if len(data_list) > 0:

                for aa in data_list:
                    expire_time_gmt = aa["expire_time_gmt"]
                    expire_time = convert_negative_timestamp(expire_time_gmt)
                    print(expire_time)
                    # date = expire_time.split(' ')[0]

                    temp = aa.get("temp")
                    dewPt = aa.get("dewPt")
                    Humidity = aa.get("rh")

                    wdir_cardinal= aa.get("wdir_cardinal")
                    wspd = aa.get("wspd")
                    gust= aa.get("gust")
                    if not gust:
                        gust=0
                    pressure = aa.get("pressure")
                    precip_total = aa.get("precip_total")
                    if not precip_total:
                        precip_total = 0
                    wx_phrase = aa.get("wx_phrase")



                    writer.writerow([expire_time, temp, dewPt, Humidity,
                                     wdir_cardinal, wspd, gust,
                                     pressure, precip_total,wx_phrase])
                print(f'Data has been written to the file')
            else:
                print(f'No data')
                break


import datetime
import pytz


def convert_time(timestamp):
   
    timestamp = int(timestamp)
    if len(str(timestamp)) == 13:
        timestamp /= 1000

    
    dt_utc = datetime.datetime.fromtimestamp(timestamp, tz=pytz.utc)

    
    arizona = pytz.timezone("US/Arizona")
    dt_arizona = dt_utc.astimezone(arizona)

    output_format = "%Y-%m-%d %H:%M:%S"
    formatted_date = dt_arizona.strftime(output_format)

    return formatted_date

def convert_negative_timestamp(timestamp):
    
    base_time = datetime.datetime(1970, 1, 1)
    offset = datetime.timedelta(seconds=abs(timestamp))

    
    if timestamp < 0:
        final_time = base_time - offset
    else:
        final_time = base_time + offset
    final_time -= datetime.timedelta(hours=9)
        
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