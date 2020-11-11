"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import crud
import server

from model import db, User, Upcominglaunch, Mylaunch, connect_to_db

from api import upcoming_launch_api

# Database setup
os.system('dropdb launchcommand')
os.system('createdb launchcommand')

connect_to_db(server.app)
db.create_all()


# CREATE LAUNCH DATABASE

launch_data = upcoming_launch_api()

# Store list of launches for later use and testing
upcoming_launch_list = []

for launch in launch_data:
    name, status_name, window_start, wiki_url, pad_location, image = (
        launch['name'], launch['status']['name'], launch['window_start'], launch['pad']['wiki_url'], launch['pad']['location']['name'], launch['image'])

    launch = crud.create_upcoming_launch(
        name=name, status_name=status_name, window_start=window_start, wiki_url=wiki_url, pad_location=pad_location, image=image)

    upcoming_launch_list.append(launch)

# TEST USERS

user1 = crud.create_user('Chris', 'Cassidy', 'cCassidy12@nasa.com',
                         'nasapass098', '3147893212')

user2 = crud.create_user('Lacey', 'Anderson', 'lAnderson13@nasa.com',
                         'nasapass123', '4147893214')


# TEST MY LAUNCH

# for saved_launch in range(3):
# user3 = crud.create_user('Lane', 'Young', 'lYoung13@nasa.com',
#                          'nasapass11', '5147893212')

# launch_choice = choice(upcoming_launch_list)
# crud.my_launch_to_db(user_id, launch_choice)

# user_launch = upcoming_launch_list[0]
# crud.my_launch_to_db(1, user_launch)
