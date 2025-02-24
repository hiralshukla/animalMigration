import pandas as pd
import plotly_express as px

import folium
from folium.plugins import HeatMap

# documentation: https://bytescout.com/blog/plotting-geographical-heatmaps-using-python-folium-library.html

map_object = folium.Map(location = [52.489471, -1.898575], zoom_start = 7 )

lat_longs = [
    [51.507351, -0.127758], # London
    [53.480759, -2.242631], # Manchester
    [53.408371, -2.991573], # Liverpool
    [52.489471, -1.898575], # Birmingham
    [51.481583, -3.179090], # Cardif
]


locations_with_popups = [{"location": [40.712776, -74.005974], "popup": "New York"},
                         {"location": [29.651634, -82.324829], "popup": "Gainesville"},
                         {"location": [27.950575, -82.457178], "popup": "Tampa"}]

HeatMap(lat_longs).add_to(map_object)

map_object.save(r"C:\Users\singu\Downloads\NWSD\map.html")



file_path = r'C:\Users\singu\Downloads\NWSD\Public.xlsx'

# chunk_size = 9000
# total_rows = 305334
#
# for start_row in range(0, total_rows, chunk_size):
#     nrows = min(chunk_size, total_rows-start_row)
#     data_sample = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=range(1, start_row + 1), nrows=nrows)
#
#     data_sample = data_sample[['LATITUDE', 'LONGITUDE']].dropna()
#     data_sample = data_sample[['LATITUDE', 'LONGITUDE']]
#     print(data_sample)
#
#     heat_data = data_sample[['LATITUDE', 'LONGITUDE']].values.tolist()
#     my_map = folium.Map(location=[data_sample['LATITUDE'].mean(),
#                         data_sample['LONGITUDE'].mean()], zoom_start=5)
#
#     HeatMap(heat_data, radius=10, max_zoom=13).add_to(my_map)
#

#
#
#     print("chunk done!")

my_map = folium.Map(location=[0, 0], zoom_start=2)  # Use the same location and zoom as the saved map
my_map = folium.Map(location=[52.489471, -1.898575], zoom_start=7)
my_map.save(r"C:\Users\singu\Downloads\NWSD\map.html")
# Add pop-ups for New York, Gainesville, and Tampa
locations_with_popups = [ {"location": [40.712776, -74.005974], "popup": "New York"}, {"location": [29.651634, -82.324829], "popup": "Gainesville"}, {"location": [27.950575, -82.457178], "popup": "Tampa"} ]
for loc in locations_with_popups:
    folium.Marker(location=loc["location"], popup=loc["popup"]).add_to(my_map)
    # Save the updated map with pop-ups
my_map.save(r"C:\Users\singu\Downloads\NWSD\my_map_with_popups.html")
