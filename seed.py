"""Script to seed database."""

import os
import requests
import json
from random import choice, randint
from datetime import datetime
import crud
import server

from model import db, User, Upcominglaunch, Mylaunch, News, My_news, connect_to_db

from api import upcoming_launch_api


# Database setup
os.system('dropdb launchcommand')
os.system('createdb launchcommand')

connect_to_db(server.app)
db.create_all()


# CREATE LAUNCH DATABASE

launch_data = upcoming_launch_api()


# TODO: refractor code
# upcomingLaunchList = launch_data.map(
#     launch => crud.createUpcomingLaunch(launch.name, launch.status.name....)
# )

for launch in launch_data:
    name, status_name, window_start, wiki_url, pad_location, image = (
        launch['name'], launch['status']['name'], launch['window_start'], launch['pad']['wiki_url'], launch['pad']['location']['name'], launch['image'])

    create_launch = crud.create_launch(
        name=name, status_name=status_name, window_start=window_start, wiki_url=wiki_url, pad_location=pad_location, image=image)


# TEST USERS

user1 = crud.create_user('Chris', 'Cassidy', 'cCassidy12@nasa.com',
                         'nasapass098', '3147893212')

user2 = crud.create_user('Lacey', 'Anderson', 'lAnderson13@nasa.com',
                         'nasapass123', '4147893214')


def news_api():
    news_res = requests.get(
        "https://test.spaceflightnewsapi.net/api/v2/articles?_limit=10")

    news_data = news_res.json()

    for dic in news_data:
        title, url, image, news_site, summary, date = (
            dic['title'], dic['url'], dic['imageUrl'], dic['newsSite'], dic['summary'], dic['publishedAt'])

        # print(title, url, image, news_site, summary, date)

        create_article = crud.create_news_article(
            title=title, url=url, image=image, news_site=news_site, summary=summary, date=date)

    return create_article
