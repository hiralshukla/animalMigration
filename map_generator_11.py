import pandas as pd
import plotly_express as px

import folium
from folium.plugins import HeatMap

# documentation: https://bytescout.com/blog/plotting-geographical-heatmaps-using-python-folium-library.html

# File path and chunking parameters for the heat map data
file_path = r'C:\Users\hiralshukla\Downloads\Public.xlsx'
chunk_size = 9000
total_rows = 305334

# Dictionary with migration information and coordinates for each city
migration_info = {
    "New York City": {
        "location": [40.712776, -74.005974],
        "info": (
            "<b>Warblers:</b> Yellow-rumped Warbler, Black-throated Blue Warbler.<br>"
            "<b>Thrushes:</b> Hermit Thrush, Swainson's Thrush.<br>"
            "<b>Sparrows:</b> White-throated Sparrows, Song Sparrows."
        )
    },
    "Chicago": {
        "location": [41.878113, -87.629799],
        "info": (
            "<b>Warblers:</b> American Redstart, Magnolia Warbler.<br>"
            "<b>Thrushes:</b> Veery, Wood Thrush.<br>"
            "<b>Sparrows:</b> Lincoln's Sparrow, Fox Sparrow."
        )
    },
    "Houston": {
        "location": [29.760427, -95.369804],
        "info": (
            "<b>Warblers:</b> Prothonotary Warbler, Yellow Warbler.<br>"
            "<b>Orioles:</b> Baltimore Orioles.<br>"
            "<b>Tanagers:</b> Summer Tanager."
        )
    },
    "Los Angeles": {
        "location": [34.052235, -118.243683],
        "info": (
            "<b>Warblers:</b> Townsend's Warbler, Wilson's Warbler.<br>"
            "<b>Flycatchers:</b> Pacific-slope Flycatcher.<br>"
            "<b>Swallows:</b> Cliff Swallow, Barn Swallow."
        )
    },
    "Atlanta": {
        "location": [33.7490, -84.3880],
        "info": (
            "<b>Warblers:</b> Black-throated Green Warbler, Pine Warbler.<br>"
            "<b>Vireos:</b> Red-eyed Vireo.<br>"
            "<b>Thrushes:</b> Gray-cheeked Thrush."
        )
    },
    "Seattle": {
        "location": [47.6062, -122.3321],
        "info": (
            "<b>Warblers:</b> Yellow Warbler, Orange-crowned Warbler.<br>"
            "<b>Flycatchers:</b> Willow Flycatcher.<br>"
            "<b>Swallows:</b> Violet-green Swallow."
        )
    },
    "Miami": {
        "location": [25.7617, -80.1918],
        "info": (
            "<b>Warblers:</b> Black-and-white Warbler, Palm Warbler.<br>"
            "<b>Swallows:</b> Bank Swallow, Barn Swallow.<br>"
            "<b>Tanagers:</b> Scarlet Tanager."
        )
    },
    "Denver": {
        "location": [39.7392, -104.9903],
        "info": (
            "<b>Warblers:</b> Yellow-rumped Warbler, MacGillivray's Warbler.<br>"
            "<b>Flycatchers:</b> Western Wood-Pewee.<br>"
            "<b>Sparrows:</b> White-crowned Sparrow."
        )
    },
    "Boston": {
        "location": [42.3601, -71.0589],
        "info": (
            "<b>Warblers:</b> Blackpoll Warbler, Northern Parula.<br>"
            "<b>Thrushes:</b> Swainson's Thrush.<br>"
            "<b>Sparrows:</b> Savannah Sparrow."
        )
    },
    "San Francisco": {
        "location": [37.7749, -122.4194],
        "info": (
            "<b>Warblers:</b> Townsend's Warbler, Hermit Warbler.<br>"
            "<b>Flycatchers:</b> Pacific-slope Flycatcher.<br>"
            "<b>Swallows:</b> Tree Swallow, Northern Rough-winged Swallow."
        )
    }
}

# Process data in chunks and add heat map layers to a new map for each chunk
for start_row in range(0, total_rows, chunk_size):
    nrows = min(chunk_size, total_rows - start_row)
    data_sample = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=range(1, start_row + 1), nrows=nrows)

    # Initialize a new map for each chunk
    overall_map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

    # Filter and clean data for latitude and longitude
    data_sample = data_sample[['LATITUDE', 'LONGITUDE']].dropna()
    heat_data = data_sample[['LATITUDE', 'LONGITUDE']].values.tolist()

    # Add heat map layer for the current chunk
    HeatMap(heat_data, radius=10, max_zoom=13).add_to(overall_map)

    # Add markers with pop-ups for each city with migration info
    for city, data in migration_info.items():
        folium.Marker(
            location=data["location"],
            popup=folium.Popup(data["info"], max_width=300),
            tooltip=city
        ).add_to(overall_map)

    # Save the final map for this chunk with a dynamic name
    chunk_number = (start_row // chunk_size) + 1
    output_file = f"C:/Users/hiralshukla/Downloads/final{chunk_number}.html"
    overall_map.save(output_file)

    print(f"Chunk {chunk_number} done! Map saved as {output_file}")
