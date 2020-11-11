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

    return render_template('login.html')


@app.route('/login')
def login():
    """User Login"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if not user:
        flash('Credentials do not exist. Please register or try again')
        return redirect('/')
    else:
        if not password:
            flash('Password is incorrect. Please try again')
            return redirect('/')
        else:
            session['current_user'] = user.user_id
            flash('Welcome!')

            # get saved launches for user and send them to their saved launch page. NOT YET CREATED.

        return render_template('/upcoming_launches')


@app.route('/register', methods=['POST'])
def register():
    """ Regiter user and save to database"""
    if request.method == 'POST':
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
        return redirect("/login")
    else:
        user = crud.create_user(fname, lname, email, phone, password)
        flash('Account created')
        return redirect('/upcoming_launches')

    return render_template('signup.html')


@app.route("/upcoming")
def upcoming_results():
    """ API results for upcoming launches route"""

    launches = crud.get_all_upcoming_launches()

    return render_template('upcoming_launches.html', launches=launches)


@app.route("/api/upcoming")
def api_results():
    """ API results"""

    data = upcoming_launch_api()

    return jsonify({'results': data})


# @app.route("/logout")
# @app.route("/user_profile")
# @app.route("/upcoming_launches")
# @app.route("/saved_launches")


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
