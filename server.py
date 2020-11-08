"""Server for launch command app"""

from jinja2 import StrictUndefined
# import crud
from model import connect_to_db
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
import requests
import json

from api import upcoming_launch_api


app = Flask(__name__)

# session secret key
app.secret_key = "launch"

app.jinja_env.undefined = StrictUndefined

#######################################
#                                     #
#                                     #
#             ROUTES                  #
#                                     #
#                                     #
#######################################


@app.route("/")
def homepage():
    """ Homepage route"""
    return render_template('homepage.html')


# TESTING THIS ONE

@app.route("/upcoming")
def upcoming_results():
    """ API results for upcoming launches route"""

    data = upcoming_launch_api()

    return render_template('upcoming_launches.html', data=data)


@app.route("/api/upcoming")
def api_results():
    """ API results"""

    data = upcoming_launch_api()

    # for launch in data:

    #     print(launch['name'])
    #     print(launch['status']['name'])
    #     print(launch['window_start'])
    #     print(launch['mission']['description'])
    #     print(launch['pad']['location']['name'])
    #     print(launch['image'])
    #     print('#####################################')

    return jsonify({'results': data})


# WORKS

# @app.route("/api/upcoming")
# def api_results():
#     """ API results"""

#     data = upcoming_launch_api()

#     return jsonify({'results': data})


# THIS ONE WORKS
# @app.route("/upcoming")
# def upcoming_results():
#     """ API results for upcoming launches route"""

#     res = requests.get(
#         "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json")

#     data = res.json()['results']

#     return render_template('upcoming_launches.html', data=data)

    # return render_template('upcoming_launches.html', data=data, id=launches[0]["name"])


# @app.route("/register_user", methods=['POST'])
# def register_user():
#     """ Regiter user and save to database"""

# fname = request.form.get('firstName')
# lname = request.form.get('lastName')
# email = request.form.get('email')
# password = request.form.get('password')
# phone = request.form.get('phone')

# return render_template('<name>.html')


# @app.route("/login")
# def login():
#     """ Login route"""
#     # return render_template('<name>.html')
# @app.route("/register_user", methods=['POST'])
# def register_user():
#     """ Regiter user and save to database"""
# fname = request.form.get('firstName')
# lname = request.form.get('lastName')
# email = request.form.get('email')
# password = request.form.get('password')
# phone = request.form.get('phone')
# return render_template('<name>.html')
# @app.route("/logout")
# @app.route("/user_profile")
# @app.route("/upcoming_launches")
# @app.route("/saved_launches")
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
