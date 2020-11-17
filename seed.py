"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import crud
import server

from model import db, User, Upcominglaunch, Mylaunch, News, My_news, connect_to_db

from api import upcoming_launch_api
from api import news_api

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


all_news = news_api()

index = 0
while index < len(all_news):

    for article in all_news[index]:

        title, url, image, news_site, summary, date = (
            all_news[index][article]['title'], all_news[index][article]['url'], all_news[index][article]['imageUrl'], all_news[index][article]['imageUrl']['newsSite'], all_news[index][article]['summary'], all_news[index][article]['publishedAt'])

        create_article = crud.create_news_article(
            title=title, url=url, image=image, news_site=news_site, summary=summary, date=date)

        index += 1
