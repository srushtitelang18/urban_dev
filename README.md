# Urban Development Analysis using OpenStreetMap

This project analyzes urban features around a specific location using OpenStreetMap data.

The system extracts and visualizes:

• Buildings  
• Road Networks  
• Parks  
• Water Bodies  

The results are displayed on an interactive map.

---

## Technologies Used

- Python
- OSMnx
- Folium
- OpenStreetMap

---

## Project Features

This project performs the following tasks:

1. Fetches urban data from OpenStreetMap.
2. Extracts buildings, roads, parks, and water bodies.
3. Displays them on an interactive map.
4. Adds a property location marker.
5. Allows switching between map layers (Satellite, Terrain, OSM).

---

## Project Location

Example coordinates used in the project:

Latitude: 12.8456  
Longitude: 77.6603  

Radius analyzed: 800 meters

---




## Installation

### Install Required Libraries

Make sure Python is installed on your system.
Then install the required libraries using pip:

```
pip install osmnx folium
```

### Verify Installation

You can check if the libraries are installed correctly by running:

```
import osmnx
import folium
```

If no error appears, the installation is successful.

---

## How to Run the Project

1. Download or clone the repository.
2. Open terminal or command prompt in the project folder.
3. Run the following command:

```
python new3.py
```

---

## Output

After running the program, the following file will be generated:

```
clean_urban_map.html
```

Open this file in a web browser to view the interactive urban analysis map.

