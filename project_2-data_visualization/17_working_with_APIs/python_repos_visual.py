import requests

from plotly.graph_objects import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"  # Line break.
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': {
        'text': 'Most-Starred Python Projects on GitHub',
        'font': {
            'family': 'Balto',
            'size': 30,
            'color': 'rgb(9, 9, 91)',
        },
        'xanchor': 'left',
        'yanchor': 'top',
    },
    'xaxis': {
        'tickfont': {'size': 14},
        'title': {
            'text': 'Repository',
            'font': {
                'family': 'Times New Roman',
                'color': 'rgb(9, 9, 91)',
                'size': 24
            },
        },
    },
    'yaxis': {
        'title': {
            'text': 'Stars',
            'font': {
                'color': 'rgb(9, 9, 91)',
                'family': 'Times New Roman',
                'size': 24,
                },
        },
        'tickfont': {'size': 14},
    },
    'paper_bgcolor': '#f8f8f8',
    'plot_bgcolor': '#dee7ed',
    'margin': {
        'b': 50,
        'l': 50,
        'r': 70,
        't': 80,
        'pad': 1
    },
    'autosize': True,
    'width': 1350,
    'height': 800
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
