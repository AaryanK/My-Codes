import geocoder

def give_location():
    return geocoder.ip('me').latlng


