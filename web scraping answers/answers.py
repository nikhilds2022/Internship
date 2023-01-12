#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
for header in headers:
    print(header.text)


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
for row in soup.select("td.titleColumn"):
    movie_name = row.a.text
    movie_year = row.span.text
    movie_rating = row.next_sibling.next_sibling.strong.text
    movies.append([movie_name, movie_year, movie_rating])

df = pd.DataFrame(movies, columns = ['Name', 'Year', 'Rating'])
print(df)


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
table = soup.find("table", {"class": "chart"})
for row in table.find_all("tr")[1:101]:
    cells = row.find_all("td")
    movie_name = cells[1].text.strip()
    movie_year = cells[2].text.strip()
    movie_rating = cells[3].text.strip()
    movies.append([movie_name, movie_year, movie_rating])

df = pd.DataFrame(movies, columns = ['Name', 'Year', 'Rating'])
print(df)


# In[4]:


import requests
from bs4 import BeautifulSoup

url = "https://presidentofindia.nic.in/former-presidents.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

presidents = []
table = soup.find("table", {"class": "table-striped"})
for row in table.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) > 0:
        name = cells[0].text.strip()
        term = cells[1].text.strip()
        presidents.append([name, term])

for president in presidents:
    print(president)


# In[5]:


import requests
from bs4 import BeautifulSoup

# Scrape top 10 ODI teams
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

teams = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    matches = cells[2].text.strip()
    points = cells[3].text.strip()
    rating = cells[4].text.strip()
    teams.append([name, matches, points, rating])

print("Top 10 ODI teams:")
for team in teams:
    print(team)

# Scrape top 10 ODI batsmen
url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

batsmen = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    batsmen.append([name, team, rating])

print("Top 10 ODI batsmen:")
for batsman in batsmen:
    print(batsman)

# Scrape top 10 ODI bowlers
url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

bowlers = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    bowlers.append([name, team, rating])

print("Top 10 ODI bowlers:")
for bowler in bowlers:
    print(bowler)


# In[6]:


import requests
from bs4 import BeautifulSoup

# Scrape top 10 ODI teams in women's cricket
url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

teams = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    matches = cells[2].text.strip()
    points = cells[3].text.strip()
    rating = cells[4].text.strip()
    teams.append([name, matches, points, rating])

print("Top 10 ODI teams in women's cricket:")
for team in teams:
    print(team)

# Scrape top 10 women's ODI Batting players
url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

batsmen = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    batsmen.append([name, team, rating])

print("Top 10 women's ODI Batting players:")
for batsman in batsmen:
    print(batsman)

# Scrape top 10 women's ODI all-rounder
url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounders"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

allrounders = []
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr")[1:11]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    allrounders.append([name, team, rating])

print("Top 10 women's ODI all-rounders:")
for allrounder in allrounders:
    print(allrounder)


# In[7]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

news = []
for article in soup.find_all("article"):
    headline = article.find("h3").text.strip()
    time = article.find("time")["datetime"]
    link = article.find("a")["href"]
    news.append([headline, time, link])

for n in news:
    print("Headline:",n[0])
    print("Time:",n[1])
    print("Link:",n[2])
    print("\n")


# In[8]:


import requests
from bs4 import BeautifulSoup

url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

articles = []
for article in soup.find_all("li", {"class":"most-downloaded-item"}):
    title = article.find("a", {"class":"title"}).text.strip()
    authors = article.find("div", {"class":"authors"}).text.strip()
    date = article.find("div", {"class":"date"}).text.strip()
    link = article.find("a", {"class":"title"})["href"]
    articles.append([title, authors, date, link])

for article in articles:
    print("Title:", article[0])
    print("Authors:", article[1])
    print("Published Date:", article[2])
    print("Link:", article[3])
    print("\n")


# In[9]:


import requests
from bs4 import BeautifulSoup

url = "https://www.dineout.co.in/mumbai-restaurants"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

restaurants = []
for div in soup.find_all("div", {"class":"listing-card"}):
    name = div.find("h3").text.strip()
    cuisine = div.find("p", {"class":"card-info__cuisine"}).text.strip()
    location = div.find("p", {"class":"card-info__location"}).text.strip()
    rating = div.find("span", {"class":"rating"}).text.strip()
    image_url = div.find("img")["src"]
    restaurants.append([name, cuisine, location, rating, image_url])

for restaurant in restaurants:
    print("Name:", restaurant[0])
    print("Cuisine:", restaurant[1])
    print("Location:", restaurant[2])
    print("Rating:", restaurant[3])
    print("Image URL:", restaurant[4])
    print("\n")


# In[10]:


import requests
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?view_op=top_venues&hl=en"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

publications = []
table = soup.find("table", {"class":"gs_table"})
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    rank = cells[0].text.strip()
    publication = cells[1].text.strip()
    h5_index = cells[2].text.strip()
    h5_median = cells[3].text.strip()
    publications.append([rank, publication, h5_index, h5_median])

for publication in publications:
    print("Rank:", publication[0])
    print("Publication:", publication[1])
    print("h5-index:", publication[2


# In[ ]:




