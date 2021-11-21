import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbmusic

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0

for song in songs:
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        rank=rank+1
        title = song.select_one('td.info > a.title.ellipsis').text.strip()
        singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank, title, singer)
        doc = {
            'rank':rank,
            'title':title,
            'singer':singer
        }
        db.songs.insert_one(doc)