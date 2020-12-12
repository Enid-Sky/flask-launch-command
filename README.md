# LAUNCH COMMAND

## Overview

Launch Command is a place for rocket enthusiasts to find the latest information on space flight news and upcoming rocket launches from around the world.  

## How the app works

On the landing page, visitors are right  away greeted by a live countdown to the next exciting rocket launch. On the upcoming launches page, users will find information on the next 10 missions. Via the Twilio API, users also have the option of receiving a text reminder of the time and date of the next exciting launch! Users also have the capability to save or delete their favorite launches and news articles from their personal libraries.

## DEMO Video
 [Launch Command](https://www.youtube.com/watch?v=ME62n_jHDP8)

## Technologies and Stack

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Jinja2
- JavaScript
- jQuery
- Bootstrap4
- HTML5
- CSS3
- [Twilio Rest API](https://www.twilio.com/docs/usage/api)
- [Launch Library 2 API](https://thespacedevs.com/llapi)
- [Spaceflight News API](https://thespacedevs.com/snapi)

## Installation instructions

- Clone or fork the repository:

  `$ git clone https://github.com/Enid-Sky/evaluate-the-news-nlp.git`

- Create and activate a virtual environment:

  `$ virtualenv env`
  `$ source env/bin/activate`

- Install dependencies:

  `pip3 install -r requirements.txt`

- Create an account with Twilio and get an API key.

- Store the key in a file names 'secrets.sh'

    `source secrest.sh`

- Using PostgreSQL create the database

    `$ createdb launchcommand`

- Create all tables and relations in the database and seed data:

    `$ python3 seed.py`

- Run the app from the command line:

    `$ python3 server.py`


  
*****


