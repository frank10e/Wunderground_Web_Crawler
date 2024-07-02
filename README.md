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

## Usage

1. Ensure you have a valid Weather Underground API key.
2. Update the API key in the script:
```python
params = {
    "apiKey": "your_api_key_here",
    # other parameters...
}