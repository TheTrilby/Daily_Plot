import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


# def mapit(projection_type, where):
map = Basemap(width=12000000, height=9000000,
    rsphere=(6378137.00,6356752.3142),
    resolution='l', area_thresh=1000., projection='lcc',
    lat_1=45., lat_2=55, lat_0=50, lon_0=-107.)

map.drawcoastlines()
map.fillcontinents(color='coral',lake_color='aqua')
map.drawparallels(np.arange(-80.,81.,20.))
map.drawmeridians(np.arange(-180.,181.,20.))
map.drawmapboundary(fill_color='aqua')

plt.title('Projection lcc because I. Am. Canadian. (Mostly for Adam Though)')

plt.savefig('2016_04_22.png')
