from utils.geo_utils import haversine

def optimize_route(data):
    locations = data["locations"]
    # Dummy optimization logic
    return sorted(locations, key=lambda x: x["lat"])
