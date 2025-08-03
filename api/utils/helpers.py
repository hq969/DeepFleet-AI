from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # Earth radius in km
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a)) 
    return R * c

def calculate_eta(origin, destination):
    """
    Calculate estimated time of arrival (ETA) in minutes
    assuming average speed of 40 km/h.
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    distance_km = haversine(lon1, lat1, lon2, lat2)
    eta_minutes = (distance_km / 40) * 60
    return round(eta_minutes, 2)
