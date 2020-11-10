"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

from api import upcoming_launch_api


os.system('dropdb launchcommand')
os.system('createdb launchcommand')

model.connect_to_db(server.app)
model.db.create_all()

# get API data
launch_data = upcoming_launch_api()

# Store launches, store them for later to user for saved launch data

upcoming_launch_list = []

for launch in launch_data:
    name, status_name, window_start, mission_description, pad_location, image = (
        launch['name'], launch['status']['name'], launch['window_start'], launch['mission']['description'], launch['pad']['location']['name'], launch['image'])

    # window_start = datetime.strptime(launch['window_start'], '%Y-%m-%d-%')
    # start = datetime.strptime()

    launch = crud.create_upcoming_launch(name=name, status_name=status_name, window_start=window_start,
                                         mission_description=mission_description, pad_location=pad_location, image=image)

    upcoming_launch_list.append(launch)


#         name = launch['name']
#         status_name = launch['status']['name']
#         window_start = launch['window_start']
#         mission_description = launch['mission']['description']
#         pad_location = launch['pad']['location']['name']
#         image = launch['image']

#
