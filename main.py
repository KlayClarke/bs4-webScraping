import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
yc_webpage_content = response.text

soup = (BeautifulSoup(yc_webpage_content, 'html.parser'))



# #accessing individual html items using BS
# article_text = article_tag.getText()
# article_link = article_tag.get('href')
# article_upvote = soup.find('span', class_='score').getText()

# accessing all similar items using BS
articles = soup.find_all('a', class_='titlelink')
for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.get('href')
    print(article_text)
    print(article_link)