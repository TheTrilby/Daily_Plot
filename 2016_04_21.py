import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def mapit(projection_type, where):
    map = Basemap(projection=projection_type, lat_0=0, lon_0=0, ax=where)
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    map.drawcoastlines()
    where.set_title('Projection Type: ' + projection_type)


all_projections = ['aeqd', 'gnom', 'ortho', 'geos', 'nsper', 'moll', 'hammer',
    'robin', 'eck4', 'kav7', 'mbtfpq', 'sinu', 'cyl', 'cass', 'merc', 'tmerc',
    'omerc', 'poly', 'mill', 'gall', 'cea', 'lcc', 'laea', 'stere', 'eqdc', 
    'aea', 'npstere', 'nplaea', 'npaeqd', 'vandg']


def flatten(rows, cols):
    ids = []
    for row in range(0,rows):
        for col in range(0,cols):
            ids.append((row,col))
    return ids

def find_ok(rows, cols, ids, projections):
    fig, ax = plt.subplots(rows, cols, figsize=(25,30))
    worked = []
    for i, projection in enumerate(projections):
        try:
            mapit(projection, ax[ids[i]])
            worked.append(projection)
        except ValueError:
            continue
    return worked



test_r = 5
test_c = 6

test_ids = flatten(test_r, test_c)
worked = find_ok(test_r, test_c, test_ids, all_projections)

r = 4
c = 5

ids = flatten(r,c)
fig, ax = plt.subplots(r, c, figsize=(20,16))
for i, projection in enumerate(worked):
    mapit(projection, ax[ids[i]])


plt.savefig('2016_04_21.png')
