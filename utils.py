import csv
import json
from collections import namedtuple

Place = namedtuple("Place", ["name", "lat", "lon"])

def read_places_from_csv(file_path):
    places = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            places.append(Place(row['Name'], float(row['Lat']), float(row['Lon'])))
    return places

def write_geojson(places, path, filename):
    coords = [[places[i].lon, places[i].lat] for i in path]
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": coords
                },
                "properties": {}
            }
        ]
    }
    with open(filename, 'w') as f:
        json.dump(geojson, f, indent=2)