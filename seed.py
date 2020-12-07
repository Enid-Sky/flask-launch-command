"""Script to seed database."""

import os
import requests
import json
from random import choice, randint
from datetime import datetime
import crud
import server

from model import db, User, Upcominglaunch, Mylaunch, News, My_news, connect_to_db

# from api import upcoming_launch_api


# Database setup
os.system('dropdb launchcommand')
os.system('createdb launchcommand')

connect_to_db(server.app)
db.create_all()


# SEED UPCOMING LAUNCH DATABASE
def upcoming_launch_api():

    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?format=json&limit=10&offset=3")

    launch_data = res.json()['results']

    for launch in launch_data:
        name, status_name, window_start, wiki_url, pad_location, image = (
            launch['name'], launch['status']['name'], launch['window_start'], launch['pad']['wiki_url'], launch['pad']['location']['name'], launch['image'])

        create_launch = crud.create_launch(
            name=name, status_name=status_name, window_start=window_start, wiki_url=wiki_url, pad_location=pad_location, image=image)

    return create_launch


# SEED USER DATABASE

user1 = crud.create_user('Chris', 'Cassidy', 'cCassidy12@nasa.com',
                         'nasapass098', '3147893212')

user2 = crud.create_user('Lacey', 'Anderson', 'lAnderson13@nasa.com',
                         'nasapass123', '4147893214')


# SEED NEWS ARTICLES DATABASE

def news_api():

    news_res = requests.get(
        "https://spaceflightnewsapi.net/api/v2/articles?_limit=15")

    news_data = news_res.json()

    for dic in news_data:
        title, url, image, news_site, summary, date = (
            dic['title'], dic['url'], dic['imageUrl'], dic['newsSite'], dic['summary'], dic['publishedAt'])

        create_article = crud.create_news_article(
            title=title, url=url, image=image, news_site=news_site, summary=summary, date=date)

    return create_article


upcoming_launch_api()
news_api()
