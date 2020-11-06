"""Server for launch command app"""

from jinja2 import StrictUndefined
# import crud
from model import connect_to_db
from flask import (Flask, render_template, request, flash, session, redirect)
import requests
import json


app = Flask(__name__)

# debug key
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


@app.route("/upcoming")
def upcoming_results():
    """ API results for upcoming launches route"""

    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json")

    data = res.json()['results']

    return render_template('upcoming_launches.html', data=data)

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
