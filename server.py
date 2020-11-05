"""Server for launch command app"""

from jinja2 import StrictUndefined
# import crud
# from model import connect_to_db
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)


app = Flask(__name__)

# debug key
app.secret_key = "launch"

app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """ Homepage route"""
    return render_template('homepage.html')


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
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

    # , port=5002
