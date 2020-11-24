"""Server for launch command app"""

from jinja2 import StrictUndefined
# import crud
from model import connect_to_db
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
import requests
import json
import crud
import datetime

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

    next_launch_start = crud.get_next_upcoming_launch()

    return render_template('homepage.html', next_launch_start=next_launch_start.window_start)


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
    return redirect('/')


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
    # time = crud.get_time()

    # x = datetime.datetime(time)
    # times = x.strftime("%c")

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

#######################################
#                                     #
#                                     #
#            News Articles            #
#                                     #
#                                     #
#######################################


@app.route('/all_news')
def all_news_results():
    """Return all news articles"""

    all_news = crud.get_all_news_articles()

    return render_template('all_news.html', all_news=all_news)


@app.route('/my_news')
def my_news_results():
    """ Return page showing all of user's saved news articles"""

    user_id = session.get('user_id')
    my_news = crud.get_saved_news_by_id(user_id)

    return render_template('my_news.html', my_news=my_news)


@app.route('/add_article', methods=['POST'])
def save_article():
    article_id = request.form.get('add_article')
    user_id = session.get('user_id')
    article = crud.save_news_article(user_id, article_id)

    name = article.news_article.title

    flash(f'{name} has been added to your news library.')

    return redirect('/all_news')


@app.route('/delete_article', methods=['POST'])
def delete_news_article():
    news_title = request.form.get('article_name')
    my_news_id = request.form.get('delete_article')
    crud.delete_news_article(my_news_id, news_title)

    flash(f'{news_title} has been deleted.')

    return redirect("/my_news")

#######################################
#                                     #
#                                     #
#            HELPER ROUTES            #
#                                     #
#                                     #
#######################################


@app.route('/data', methods=['GET', 'POST'])
def get_data():

    # GET request
    if request.method == 'GET':
        db_data = crud.get_next_upcoming_launch()
        db_data_2 = crud.get_next_next_upcoming_launch()
        date = db_data.window_start
        name = db_data.name
        second_launch = db_data_2.window_start
        second_name = db_data_2.name
        message = {'date': date, 'name': name,
                   'second_launch': second_launch, 'second_name': second_name}
        print(message)
        return jsonify(message)

    # POST request
    if request.method == 'POST':
        print(request.get_json())
        return 'Success', 200


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
