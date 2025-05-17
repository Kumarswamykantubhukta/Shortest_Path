import argparse
from utils import read_places_from_csv, write_geojson
from distance import compute_distance_matrix
from tsp_solver import greedy_tsp_solver, two_opt, path_distance

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', required=True, help='CSV file with places')
    parser.add_argument('--start', required=True, help='Start location name')
    parser.add_argument('--return_', dest='return_to_start', action='store_true', help='Return to start point')
    # For quick testing without CLI
    args = parser.parse_args([
    '--csv', 'places.csv',
    '--start', 'Hyderabad',
    '--return_'
     ])


    places = read_places_from_csv(args.csv)
    dist = compute_distance_matrix(places)
    name_to_index = {place.name: i for i, place in enumerate(places)}

    if args.start not in name_to_index:
        print("Available places:", list(name_to_index.keys()))  # Debugging aid
        raise ValueError(f"Start place '{args.start}' not found in CSV")

    start_index = name_to_index[args.start]
    path = greedy_tsp_solver(places, dist, start_index)
    path = two_opt(path, dist)

    if args.return_to_start:
        path.append(start_index)

    total_dist = path_distance(path, dist)

    print("Optimal tour (returns to start if specified):")
    for i in path:
        print(f"- {places[i].name}")
    print(f"Total distance: {total_dist:.1f} km")

    write_geojson(places, path, 'route.geojson')
    print("Route written to route.geojson")
    
main()