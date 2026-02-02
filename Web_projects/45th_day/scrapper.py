import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()

news_site_text= response.text # no json
soup = BeautifulSoup(news_site_text,"html.parser")
articles = soup.find_all(name="a",class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

a_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

news_map = {score:{news_title,news_link} for score,news_title,news_link in zip(a_score,article_texts,article_links)}

sorted_news_map = dict(sorted(news_map.items(),reverse=True))
print(list(sorted_news_map.items())[0])