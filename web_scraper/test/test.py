#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

main_url = "https://mangareader.to/completed?sort=most-viewed"
response = requests.get(main_url)
response_text = response.text

soup = BeautifulSoup(response_text, "lxml")
# print(soup.title.text)

mangaDict = {}

mangas = soup.find_all("h3", class_="manga-name")
genres = soup.find_all("div", class_="fd-infor")

# i = 1
# for manga in mangas:
#     for genre in genres:
#         mangaDict[i] = {"manga_name": manga.text, "genre": [genre.text.strip()]}
#     i += 1

for genre in genres:
    print(genre.text.strip())

# print(mangaDict)