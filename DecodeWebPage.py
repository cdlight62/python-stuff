import requests
from bs4 import BeautifulSoup

def get_article_titles():
    r = requests.get("http://www.nytimes.com/")
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    title = [x.string.strip() for x in soup.find_all('h2', 'story-heading') if x.string is not None]
    return title

with open('article_titles', 'w') as open_file:
    open_file.write('\n'.join(get_article_titles()))