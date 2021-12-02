import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
yc_webpage_content = response.text

soup = (BeautifulSoup(yc_webpage_content, 'html.parser'))

article_tag = soup.find('a', class_='titlelink')
article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find('span', class_='score').getText()
