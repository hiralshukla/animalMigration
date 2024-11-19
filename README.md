![animalMigration](animalMigration.png)

# Federal Aviation Association Migratory Bird Visualizer

# Table of Contents
- [What is the Migratory Bird Visualizer?](#what-is-the-migratory-bird-visualizer)
- [Installation](#installation)
- [Instructions](#instructions)
- [Commands](#commands)
- [How HeatMaps are Made](#how-heatmaps-are-made)
- [Contributing](#contributing)

# What is the Migratory Bird Visualizer?
This visualizer prototype uses Python to create heatmaps!
Maps 1-11 are all 9000 data points each, to ensure it is less memory intensive.
Each contains data from 1990 - 2011.
The FAA organizes their datasets using IDs per incident, which also have been used here!
Map 12 contains 45000+ data points mapping the lat. & long. of bird strikes.
I hope this project encourages avian conservation & research <3!

Data collection and organization, graphing, and user interface is all done in Python.
The maps and documentation are all displayed using HTML.

Prototype released 11/19/2024

# Installation
Ensure you have the following:
- Python 3.10+
- Windows 10 PowerShell
- install necessary python packages using pip
- run using python main.py

# Instructions
- fork the repository
- download the files from the repository locally
- open Windows 10 PowerShell
- go to the file in your computer and run python main.py

# Commands
Inputting these commands into the terminal will cause an action:
- exit: end program
- docs: shows faa documentation
- faa: FAA website
- profHVZ: get to know Dr. Hannah Vander Zanden
- pydocs: shows python documentation
 -animalMigration: thank you message
- hiral: get to know me!
- 1-12: displays heatmap/visualization

![heatMap](heatMap.png)

# How HeatMaps are Made
## Features:
- **Interactive Heatmaps:** Utilizes latitude and longitude values recorded of each strike to create detailed heatmaps using Folium and traversing the FAA Excel file.
- **Informational Popups:** All major hotspots/airports are plotted with a popup regarding their migratory birds.
- **Extensive Data Coverage:** Maps 1-11 contain 9000 data points each, covering incidents from 1990 to 2011. Map 12 includes over 45000 data points, providing a comprehensive view of bird strike incidents.

The heatmaps are under-representative of the total number of bird strikes as those reprted without location data were not able to be plotted on the graph. The goal of the project is in the future being about to plot all data up till 2024 which would be 300000 data points. 

# Contributing
Contact me at hiralshukla@ufl.edu

  
  



  

  
