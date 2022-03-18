import requests

from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=topic:ukraine&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore info on the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Take a look at the first repo.
repo_dict = repo_dicts[0]

print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Watchers: {repo_dict['watchers_count']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Forks: {repo_dict['forks']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Language: {repo_dict['language']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Topics: {repo_dict['topics']}")

# Process results.
repo_links, stars, watchers, forks, labels, language = [], [], [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    watchers.append(repo_dict['watchers_count'])
    forks.append(repo_dict['forks'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
    language.append(repo_dict['language'])
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
        'text': 'Most-Starred Projects Related to Ukraine',
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
offline.plot(fig, filename='ukraine_repos.html')
