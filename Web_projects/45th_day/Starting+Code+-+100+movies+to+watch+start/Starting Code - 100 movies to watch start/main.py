import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

response.raise_for_status()

soup = BeautifulSoup(response.text,"html.parser")

articles = soup.find_all(name="h3",class_="title")
movie_list:list = []

for article in reversed(articles):
    movie_list.append(article.text)

movies_string = '\n'.join(movie_list)
print(movies_string)

with open("Web_projects\\45th_day\Starting+Code+-+100+movies+to+watch+start\Starting Code - 100 movies to watch start\movies.txt","w", encoding="utf-8") as file:
    file.write(movies_string)


