import json

from matplotlib.pyplot import title

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import os

os.chdir('C:/Users/Felipe/python_work/notebooks/bk_Python_crash_course/' +
         'project_2-data_visualization/16_downloading_data')


filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes cursomizing marker size according to mag sizes.
# Create a dict with Scattergo object.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [4*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title='Global Earthquakes')  # Title

fig = {'data': data, 'layout': my_layout}  # Dictionary with data and layout.
# Pass fig to the plot() function and add descriptive filename.
offline.plot(fig, filename='global_earthquakes.html')
