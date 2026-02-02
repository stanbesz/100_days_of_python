from bs4 import BeautifulSoup

with open("./Web_projects\\45th_day\\bs4-start\\bs4-start\website.html","r") as file:
    soup = BeautifulSoup(file, 'html.parser')

#print(soup)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

#heading = soup.find(name="h1",id="name")
section_heading = soup.find(name="h3",class_="heading") 
'class is a special keyword in Python, that is why we use class_'
print(section_heading)

'uses the css selector to target an element'
a_select = soup.select_one(selector="p a")
print(a_select)