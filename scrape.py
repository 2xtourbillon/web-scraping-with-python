"""
this script looks at the first 2 pages of hackernews and pulls the stories
scores over 99 to create a list of dictionaries.
"""

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')


mega_links = links + links2
mega_subtext = subtext + subtext2

# create a function to sort the hn list of dictionaries by the votes
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

# create a function to pull in the title, link and votes;
# add the links only if the votes are over 99
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points>99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# pretty print the result
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
