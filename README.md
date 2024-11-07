# Wunderground_Web_Crawler

# Wunderground Weather Data Crawler

## Project Overview

This project is a Python-based web crawler designed to fetch historical weather data from the Weather Underground (Wunderground) website. It automatically collects detailed meteorological information from 1949 to the present day, organizing the data into an easily analyzable CSV format.

## Key Features

- Automated retrieval of long-term historical weather data (from 1949 to present)
- Support for multiple meteorological parameters including temperature, dew point, humidity, pressure, wind speed, and precipitation
- Data presented as daily maximum, minimum, and average values
- Results saved in CSV format for easy analysis and visualization

## Tech Stack

- Python 3.x
- Dependencies:
  - requests: For sending HTTP requests
  - csv: For handling CSV files
  - datetime: For date and time operations
  - pytz: For timezone conversions

## Easy Way to do

- If you only want to crawl the history of a specific Wunderground site, all you need to do is download the python file Wunderground_Web_Perp_Easy_To_Do.py and change the states_ids to the name of the site that Wunderground displays above, and set the station_names to the name you want. If you want to change the crawling date range, you need to change the start_date and end_date, the default is from January 1st, 2024 to September 1st, 2024

