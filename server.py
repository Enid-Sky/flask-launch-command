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
    else:
        user = crud.create_user(fname, lname, email, phone, password)
        session['user_id'] = user.user_id
        session['email'] = user.email
        flash('Account created! Please sign into your account')
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    """User Login"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if password == '' or email == '':
        flash('Sorry, login failed. Please try again.')
        return redirect("/")

    if user:
        session['user_id'] = user.user_id
        session['email'] = user.email
        flash(f'Welcome back, {user.fname}!')
        return redirect('/upcoming')

    else:
        flash('Either email or password are incorrect. Please try again.')
        return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out')
    return render_template('homepage.html')


#######################################
#                                     #
#                                     #
#              Launches               #
#                                     #
#                                     #
#######################################


@app.route('/upcoming')
def upcoming_results():
    """ Return page showing all upcoming launches"""

    launches = crud.get_all_upcoming_launches()

    return render_template('upcoming_launches.html', launches=launches)


@app.route('/my_launches')
def my_launch_results():
    """ Return page showing all of user's saved launches"""

    user_id = session.get('user_id')
    my_launches = crud.get_saved_by_id(user_id)

    return render_template('my_launches.html', my_launches=my_launches)


@app.route('/add_launch', methods=['POST'])
def add_a_launch():

    launch_id = request.form.get('launch')
    user_id = session.get('user_id')
    launch = crud.my_launch_to_db(user_id, launch_id)

    name = launch.launch.name
    flash(f'You are now following the upcoming launch for {name}')

    return redirect("/upcoming")


@app.route('/delete_launch', methods=['POST'])
def delete_a_launch():
    launch_name = request.form.get('launch_name')
    my_launch_id = request.form.get('delete_launch')
    crud.delete_my_launch(my_launch_id, launch_name)

    flash(f'{launch_name} has been unfollowed.')

    return redirect("/my_launches")


# @app.route('/addtocart', methods='POST'])q
# def add_to_cart();
#     """Add new launch to user's follow list"""

#     user_id = session.get('user_id')
#     launch_id = request.form.get('thevalue')


#     return render_template('saved_launches.html', user_id=user_id, )

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
