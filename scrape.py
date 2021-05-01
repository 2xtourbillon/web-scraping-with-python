import requests
import bs4

res = requests.get("https://news.ycombinator.com/")

print(res.text)
