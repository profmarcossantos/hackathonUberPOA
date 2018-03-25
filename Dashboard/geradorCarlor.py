import random
'''
for i in range (0,500):
    latitude = random.uniform(-30, -30.1)
    longitude = random.uniform(-51.1, -51.2)
    print("new google.maps.LatLng("+str(latitude)+", "+str(longitude)+"),")
'''
'''
for i in range (0,500):
    latitude = random.uniform(-30.0555, -30.07)
    longitude = random.uniform(-51.15555, -51.19)
    print("new google.maps.LatLng("+str(latitude)+", "+str(longitude)+"),")

'''
'''
print('{ "coordenadas": [')
for i in range (0,500):
    latitude = random.uniform(-30.0555, -30.07)
    longitude = random.uniform(-51.15555, -51.19)
    print('{"lat":'+str(latitude)+', "lng":'+str(longitude)+"},")
print("]}")
    latitude = random.uniform(-30.0540983, -30.0632533)
    longitude = random.uniform(-51.1943688, -51.2095608)

'''
latitudeInicial = -30.0540776
latitudeFinal = -30.0632533
longitudeInicial = -51.2008488
longitudeFinal = -51.2095608
for i in range (0,16):
    latitude = latitudeInicial - 0.00064 * i
    longitude = longitudeInicial + 0.001 * i
    print("new google.maps.LatLng("+str(latitude)+", "+str(longitude)+"),")
    for x in range(0,10):
        latitude = latitude + (latitude*0.0000010)
        longitude = longitude + (longitude*0.0000010)
        print("new google.maps.LatLng("+str(latitude)+", "+str(longitude)+"),")
