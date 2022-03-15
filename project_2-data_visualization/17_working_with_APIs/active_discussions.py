from operator import itemgetter

import requests
from plotly.graph_objects import Bar
from plotly import offline


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # This is a special YC post with comments disabled.
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Generates lists for plotting.
titles, num_comments, discn_links = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    hn_link = submission_dict['hn_link']
    discn_link = f"<a href='{hn_link}'>{title[:15]}...</a>"

    titles.append(title)
    num_comments.append(submission_dict['comments'])
    discn_links.append(discn_link)

# Make a visualization
data = [{
    'type': 'bar',
    'x': discn_links,
    'y': num_comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': {
        'text': 'Most Active Discussions on Hacker News Right Now',
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
            'text': 'Article',
            'font': {
                'family': 'Times New Roman',
                'color': 'rgb(9, 9, 91)',
                'size': 24
            },
        },
    },
    'yaxis': {
        'title': {
            'text': 'Number of Comments',
            'font': {
                'color': 'rgb(9, 9, 91)',
                'family': 'Times New Roman',
                'size': 24,
            },
        },
        'tickfont': {'size': 14}
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
offline.plot(fig, filename='hacker_news_discussions.html')
