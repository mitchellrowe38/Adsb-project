import math
homeLat=37.573479815961754
homeLon=-122.35196945176196

def bearing_deg(lat1, lon1, lat2, lon2):
    
    lat1rad=math.radians(lat1)
    lon1rad=math.radians(lon1)
    lat2rad=math.radians(lat2)
    lon2rad=math.radians(lon2)
    #initial bearing formula
    bearing=math.atan2(math.sin(lon2rad-lon1rad)*math.cos(lat2rad),
                       math.cos(lat1rad)*math.sin(lat2rad)-math.sin(lat1rad)
                       *math.cos(lat2rad)*math.cos(lon2rad-lon1rad))
    return(math.degrees(bearing)+360)%360
print(bearing_deg(homeLat,homeLon,37.58298694194056,-122.33944674532542))


    