"""Server for launch command app"""

from jinja2 import StrictUndefined
# import crud
from model import connect_to_db
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
import requests
import json
import crud

from api import upcoming_launch_api


app = Flask(__name__)

# session secret key
app.secret_key = "COMMAND"

app.jinja_env.undefined = StrictUndefined


#######################################
#                                     #
#                                     #
#               USERS                 #
#                                     #
#                                     #
#######################################


@app.route("/")
def homepage():
    """ Homepage route"""

    return render_template('homepage.html')


@app.route('/register')
def create_user():

    return render_template('signup.html')


@app.route('/', methods=['POST'])
def register():
    """ Register user and save to database"""

    fname = request.form.get('firstName')
    lname = request.form.get('lastName')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    # check to see if user already exists
    user = crud.get_user_by_email(email)

    # if already exists, ask to sign in
    if user:
        flash('This email already exists. Please sign in.')
        return redirect("/")
    elif not user:
        user = crud.create_user(fname, lname, email, phone, password)
        if user:
            session['user_id'] = user.user_id
        return redirect('/upcoming')
    else:
        flash('Signup could not be completed. Please try again.')


@app.route('/login', methods=['POST'])
def login():
    """User Login"""

    email = request.form.get('email')
    password = request.form.get('password')

    current_user = crud.get_user_by_email(email)

    if current_user and current_user.password == password:
        flash('Welcome!')

        return redirect('/upcoming')
    else:
        flash('Either email or password are incorrect')
        return redirect('/')


#######################################
#                                     #
#                                     #
#              Launches               #
#                                     #
#                                     #
#######################################

@app.route("/upcoming")
def upcoming_results():
    """ Return page showing all upcoming launches"""

    launches = crud.get_all_upcoming_launches()

    return render_template('upcoming_launches.html', launches=launches)


# @app.route("/my_launches")
# def user_saved_launches():

    # @app.route("/api/upcoming")
    # def api_results():
    #     """ API results"""

    #     data = upcoming_launch_api()
    #     return jsonify({'results': data})
    # @app.route("/logout")
    # @app.route("/user_profile")
    # @app.route("/upcoming_launches")
    # @app.route("/saved_launches")
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
