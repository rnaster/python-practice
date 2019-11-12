"""
example of operator module
"""
from operator import itemgetter, attrgetter
from collections import namedtuple

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.68, 139.69)),
    ('Delhi NCR', 'IN', 21.935, (28.61, 77.20)),
    ('Mexico City', 'MX', 20.132, (19.43, -99.13)),
    ('New York-Newark', 'US', 20.104, (40.80, -74.02)),
    ('Sao Paulo', 'BR', 19.64, (-23.54, -46.63))
]

# ex of itemgetter
# use lambda
for city in sorted(metro_data, key=lambda x: x[1]):
    print(city)
print()

# use itemgetter
cc_name = itemgetter(1, 2, 0)
for city in sorted(metro_data, key=itemgetter(1)):
    print(cc_name(city))
print()

# ex of attrgetter
lat_long = namedtuple('LatLong', 'lat long')
metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_area = [metropolis(name, cc, pop, lat_long(lat, long))
              for name, cc, pop, (lat, long) in metro_data]
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_area, key=attrgetter('coord.lat')):
    print(name_lat(city))
print()
