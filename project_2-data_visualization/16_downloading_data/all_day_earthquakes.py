import json

from matplotlib.pyplot import title

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import os

os.chdir('C:/Users/Felipe/python_work/notebooks/bk_Python_crash_course/' +
         'project_2-data_visualization/16_downloading_data')


filename = 'data/all_day_earthquakes_3-7-2022.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(int(eq_dict['properties']['mag']))
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])


# Map the earthquakes cursomizing marker size according to mag sizes.
# Create a dict with Scattergo object.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title=title)  # Title

fig = {'data': data, 'layout': my_layout}  # Dictionary with data and layout.
# Pass fig to the plot() function and add descriptive filename.
offline.plot(fig, filename='global_earthquakes.html')
