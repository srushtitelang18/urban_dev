import osmnx as ox
import folium

# =====================================
# PROPERTY LOCATION
# =====================================

lat = 12.8456
lon = 77.6603
radius = 800

print("Fetching urban data...")

# =====================================
# FETCH DATA FROM OSM
# =====================================

tags = {
    "building": True,
    "highway": True,
    "leisure": ["park"],
    "natural": ["water"]
}

features = ox.features_from_point((lat, lon), tags=tags, dist=radius)

# Separate layers
buildings = features[features["building"].notna()] if "building" in features else []
roads = features[features["highway"].notna()] if "highway" in features else []
parks = features[features["leisure"] == "park"] if "leisure" in features else []
water = features[features["natural"] == "water"] if "natural" in features else []

# =====================================
# CREATE MAP
# =====================================

m = folium.Map(location=[lat, lon], zoom_start=15, tiles=None)

# OpenStreetMap
folium.TileLayer(
    "OpenStreetMap",
    name="OpenStreetMap"
).add_to(m)

# Satellite layer
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Satellite"
).add_to(m)

# Terrain layer
folium.TileLayer(
    tiles="https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg",
    attr="Map tiles by Stamen Design",
    name="Terrain"
).add_to(m)

# Light map
folium.TileLayer(
    "CartoDB Positron",
    name="Light Map"
).add_to(m)

# =====================================
# ROAD NETWORK
# =====================================

road_layer = folium.FeatureGroup(name="Road Network")

for geom in getattr(roads, "geometry", []):

    if geom.geom_type in ["LineString", "MultiLineString"]:

        folium.GeoJson(
            geom,
            style_function=lambda x: {
                "color": "blue",
                "weight": 2
            }
        ).add_to(road_layer)

road_layer.add_to(m)

# =====================================
# BUILDINGS
# =====================================

building_layer = folium.FeatureGroup(name="Buildings")

for geom in getattr(buildings, "geometry", []):

    if geom.geom_type in ["Polygon", "MultiPolygon"]:

        folium.GeoJson(
            geom,
            style_function=lambda x: {
                "color": "orange",
                "fillOpacity": 0.6
            }
        ).add_to(building_layer)

building_layer.add_to(m)

# =====================================
# PARKS
# =====================================

park_layer = folium.FeatureGroup(name="Parks")

for geom in getattr(parks, "geometry", []):

    if geom.geom_type in ["Polygon", "MultiPolygon"]:

        folium.GeoJson(
            geom,
            style_function=lambda x: {
                "color": "green",
                "fillOpacity": 0.5
            }
        ).add_to(park_layer)

park_layer.add_to(m)

# =====================================
# WATER BODIES
# =====================================

water_layer = folium.FeatureGroup(name="Water Bodies")

for geom in getattr(water, "geometry", []):

    if geom.geom_type in ["Polygon", "MultiPolygon"]:

        folium.GeoJson(
            geom,
            style_function=lambda x: {
                "color": "cyan",
                "fillOpacity": 0.6
            }
        ).add_to(water_layer)

water_layer.add_to(m)

# =====================================
# PROPERTY MARKER
# =====================================

folium.Marker(
    [lat, lon],
    popup="Property Location",
    icon=folium.Icon(color="red", icon="home")
).add_to(m)

# =====================================
# BUFFER ZONE
# =====================================

folium.Circle(
    location=[lat, lon],
    radius=radius,
    color="green",
    fill=False
).add_to(m)

# =====================================
# LAYER CONTROL
# =====================================

folium.LayerControl(collapsed=False).add_to(m)

# =====================================
# SAVE MAP
# =====================================

m.save("clean_urban_map.html")

print("Map created successfully!")
print("Saved as: clean_urban_map.html")