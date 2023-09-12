import json
import pandas as pd 
import numpy as np

def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


# Opening JSON file
f = open('port_arthur.json')
 
# returns JSON object as a dictionary
data = json.load(f)
 
# Flatten each dictionary and store the results in a list
flattened_dicts = [flatten_dict(d) for d in data['data']]

# Create a DataFrame
data = pd.DataFrame(flattened_dicts)

# Print the DataFrame
print(data)
 
# Closing file
f.close()
data['navigation_time'] = pd.to_datetime(data['navigation_time'])

data = data[data['navigation_status'] != 'moored'].drop_duplicates()

tugs = data.loc[(data['vessel_type'] == 'tug')]
non_tug = data.loc[(data['vessel_type'] != 'tug')]
merged_data = non_tug.merge(tugs,how= 'cross', suffixes = ('_nontug','_tug'))
merged_data['time_diff'] = (merged_data['navigation_time_tug']-merged_data['navigation_time_nontug']).dt.total_seconds() / 60

# Function to calculate distance in kilometers using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = R * c
    
    return distance

# Apply the haversine function to each row to create a new column 'distance_km'
merged_data['distance_km'] = merged_data.apply(lambda row: haversine(row['navigation_location_lat_nontug'], row['navigation_location_long_nontug'], row['navigation_location_lat_tug'], row['navigation_location_long_tug']), axis=1)

merged_data
tugged_vessels = merged_data[(abs(merged_data['time_diff']) < 10) & (merged_data['distance_km'] < 0.5 )]
tugged_vessels 