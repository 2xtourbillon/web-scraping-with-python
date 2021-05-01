import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn

print(create_custom_hn(links, subtext))
