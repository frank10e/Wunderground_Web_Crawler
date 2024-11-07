import datetime
import pandas as pd
from wunderground_pws import WUndergroundAPI, units

# Initialize the WUndergroundAPI object with your API key
wu = WUndergroundAPI(
    api_key='e1f10a1e78da46f5b10a1e78da96f525',  
    units=units.ENGLISH_UNITS,
)

# Define the station IDs and names you want to fetch data for
station_ids = ['KAZGREEN205', 'KAZGREEN153', 'KAZGREEN159', 'KAZGREEN285', 'KAZGREEN122', 
               'KAZSAHUA98', 'KAZGREEN85', 'KAZGREEN131', 'KAZGREEN218', 'KAZGREEN293', 
               'KAZGREEN232', 'KAZGREEN95', 'KAZGREEN251', 'KAZSAHUA100', 'KAZSAHUA109', 
               'KAZSAHUA60', 'KAZSAHUA117', 'KAZGREEN99', 'KAZSAHUA74', 'KAZSAHUA102', 
               'KAZSAHUA105', 'KAZGREEN181', 'KAZGREEN241', 'KAZGREEN281', 'KAZGREEN299', 
               'KAZGREEN140', 'KAZGREEN174', 'KAZGREEN233', 'KAZGREEN129', 'KAZGREEN177', 
               'KAZGREEN168', 'KAZGREEN46', 'KAZGREEN180', 'KAZGREEN269', 'KAZGREEN71', 
               'KAZGREEN227', 'KAZGREEN48', 'KAZGREEN166', 'KAZGREEN25', 'KAZGREEN204', 
               'KAZGREEN265', 'KAZGREEN297', 'KAZGREEN141', 'KAZGREEN175', 'KAZGREEN53', 
               'KAZGREEN244', 'KAZGREEN266', 'KAZGREEN143', 'KAZGREEN221', 'KAZGREEN229', 
               'KAZGREEN151', 'KAZGREEN261', 'KAZGREEN258', 'KAZGREEN82', 'KAZGREEN201', 
               'KAZGREEN88', 'KAZGREEN253', 'KAZGREEN290', 'KAZGREEN176', 'KAZGREEN61', 
               'KAZGREEN15', 'KAZSONOI59', 'KAZVAIL289', 'KAZVAIL185', 'KAZVAIL66', 
               'KAZVAIL205', 'KAZVAIL258', 'KAZVAIL273', 'KAZVAIL112', 'KAZVAIL252', 
               'KAZVAIL210', 'KAZVAIL259', 'KAZVAIL196', 'KAZVAIL173', 'KAZVAIL185', 
               'KAZCORON6', 'KAZVAIL134', 'KAZVAIL65', 'KAZVAIL288', 'KAZVAIL214', 
               'KAZVAIL71', 'KAZCORON16', 'KAZCORON7', 'KAZVAIL226', 'KAZVAIL76', 
               'KAZCORON22', 'KAZVAIL203', 'KAZVAIL270', 'KAZVAIL276', 'KAZSAHUA112', 
               'KAZSAHUA88', 'KAZSAHUA24', 'KAZSAHUA103', 'KAZSAHUA32', 'KAZSAHUA55', 
               'KAZSAHUA42', 'KAZSAHUA101', 'KAZSAHUA43', 'KAZSAHUA45', 'KAZSAHUA108', 
               'KAZSAHUA99', 'KAZSAHUA80', 'KAZSONOI59', 'KAZGREEN294', 'KAZAMADO2', 
               'KAZAMADO15']

# Define the station names
station_names = ['KAZGREEN205', 'KAZGREEN153', 'KAZGREEN159', 'KAZGREEN285', 'KAZGREEN122', 
                 'KAZSAHUA98', 'KAZGREEN85', 'KAZGREEN131', 'KAZGREEN218', 'KAZGREEN293', 
                 'KAZGREEN232', 'KAZGREEN95', 'KAZGREEN251', 'KAZSAHUA100', 'KAZSAHUA109', 
                 'KAZSAHUA60', 'KAZSAHUA117', 'KAZGREEN99', 'KAZSAHUA74', 'KAZSAHUA102', 
                 'KAZSAHUA105', 'KAZGREEN181', 'KAZGREEN241', 'KAZGREEN281', 'KAZGREEN299', 
                 'KAZGREEN140', 'KAZGREEN174', 'KAZGREEN233', 'KAZGREEN129', 'KAZGREEN177', 
                 'KAZGREEN168', 'KAZGREEN46', 'KAZGREEN180', 'KAZGREEN269', 'KAZGREEN71', 
                 'KAZGREEN227', 'KAZGREEN48', 'KAZGREEN166', 'KAZGREEN25', 'KAZGREEN204', 
                 'KAZGREEN265', 'KAZGREEN297', 'KAZGREEN141', 'KAZGREEN175', 'KAZGREEN53', 
                 'KAZGREEN244', 'KAZGREEN266', 'KAZGREEN143', 'KAZGREEN221', 'KAZGREEN229', 
                 'KAZGREEN151', 'KAZGREEN261', 'KAZGREEN258', 'KAZGREEN82', 'KAZGREEN201', 
                 'KAZGREEN88', 'KAZGREEN253', 'KAZGREEN290', 'KAZGREEN176', 'KAZGREEN61', 
                 'KAZGREEN15', 'KAZSONOI59', 'KAZVAIL289', 'KAZVAIL185', 'KAZVAIL66', 
                 'KAZVAIL205', 'KAZVAIL258', 'KAZVAIL273', 'KAZVAIL112', 'KAZVAIL252', 
                 'KAZVAIL210', 'KAZVAIL259', 'KAZVAIL196', 'KAZVAIL173', 'KAZVAIL185', 
                 'KAZCORON6', 'KAZVAIL134', 'KAZVAIL65', 'KAZVAIL288', 'KAZVAIL214', 
                 'KAZVAIL71', 'KAZCORON16', 'KAZCORON7', 'KAZVAIL226', 'KAZVAIL76', 
                 'KAZCORON22', 'KAZVAIL203', 'KAZVAIL270', 'KAZVAIL276', 'KAZSAHUA112', 
                 'KAZSAHUA88', 'KAZSAHUA24', 'KAZSAHUA103', 'KAZSAHUA32', 'KAZSAHUA55', 
                 'KAZSAHUA42', 'KAZSAHUA101', 'KAZSAHUA43', 'KAZSAHUA45', 'KAZSAHUA108', 
                 'KAZSAHUA99', 'KAZSAHUA80', 'KAZSONOI59', 'KAZGREEN294', 'KAZAMADO2', 
                 'KAZAMADO15']

# Define the date range for data retrieval
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 9, 1)

# Loop through each station to fetch data
for i in range(len(station_ids)):
    station_id = station_ids[i]
    station_name = station_names[i]
    
    print(f"\nFetching data for {station_name} ({station_id})\n")
    
    all_imperial_data = []
    current_date = start_date
    

    while current_date <= end_date:
        try:
            response = wu.history(date=current_date, station_id=station_id, granularity='daily')
            
            
            if 'observations' in response and len(response['observations']) > 0:
                imperial_data = response['observations'][0]['imperial']
                imperial_data['date'] = current_date
                all_imperial_data.append(imperial_data)
            else:
                print(f"No data for {current_date}")
        
        except Exception as e:
            print(f"Error fetching data for {current_date} at {station_name}: {e}")
        
        
        current_date += datetime.timedelta(days=1)
    
    if all_imperial_data:
        df = pd.DataFrame(all_imperial_data)
        csv_filename = f"{station_name}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}")
    else:
        print(f"No data available for {station_name}")
