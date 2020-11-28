"""CRUD operations"""

import datetime
from model import db, User, Upcominglaunch, Mylaunch, News, My_news, connect_to_db
from api import upcoming_launch_api


#######################################
#                                     #
#                                     #
#               USERS                 #
#                                     #
#                                     #
#######################################


def create_user(fname, lname, email, password, mobile_number):

    # create a user
    user = User(fname=fname, lname=lname, email=email,
                password=password, mobile_number=mobile_number)

    # add user to database
    db.session.add(user)
    db.session.commit()

    print('::user created::')

    return user


def get_user_by_id(user_id):
    """Return a user by id"""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()


#######################################
#                                     #
#                                     #
#              Launches               #
#                                     #
#                                     #
#######################################


def create_launch(name, status_name, window_start, wiki_url, pad_location, image):

    # create a launch
    launch = Upcominglaunch(name=name, status_name=status_name,
                            window_start=window_start, wiki_url=wiki_url, pad_location=pad_location, image=image)

    # save launch to database
    db.session.add(launch)
    db.session.commit()

    print('::create upcoming launch::')

    return launch


def get_all_upcoming_launches():
    """Return all launches to display on upcoming launches page"""

    return Upcominglaunch.query.all()


def get_time():
    """Return all datetimes for upcoming launches"""

    time = db.session.query(Upcominglaunch.window_start).all()

    return time


def my_launch_to_db(user_id, launch_id):
    """Create and return launch that has been saved by session user"""

    saved_launch = Mylaunch(
        user_id=user_id, launch_id=launch_id)

    db.session.add(saved_launch)
    db.session.commit()

    return saved_launch


def delete_my_launch(my_launch_id, launch_name):
    """Remove a user's saved launch from the database"""

    delete_launch = Mylaunch.query.get(my_launch_id)

    db.session.delete(delete_launch)
    db.session.commit()

    return launch_name


def get_saved_by_id(user_id):
    """Find launch that has been saved by session user"""

    return Mylaunch.query.filter(Mylaunch.user_id == user_id).all()


def get_all_saved_by_id(user_id):
    """Find all launches that have been saved by session user"""

    launch_ids = []
    user_saved_launches = Mylaunch.query.filter(
        Mylaunch.user_id == user_id).all()

    for launch in user_saved_launches:
        launch_ids.append(launch.launch_id)
    return launch_ids


def get_next_upcoming_launch():
    """Return next upcoming launch to display in countdown"""

    next_launch_time = Upcominglaunch.query.get(1)

    return next_launch_time


def get_next_next_upcoming_launch():
    """Return next upcoming launch to display in countdown"""

    next_next_launch_time = Upcominglaunch.query.get(2)

    return next_next_launch_time


#######################################
#                                     #
#                                     #
#            News Articles            #
#                                     #
#                                     #
#######################################


def create_news_article(title, url, image, news_site, summary, date):

    # create a news article
    news_item = News(title=title, url=url, image=image,
                     news_site=news_site, summary=summary, date=date)

    # save news article to database
    db.session.add(news_item)
    db.session.commit()

    print('::create news article,::')

    return news_item


def get_all_news_articles():
    """Return all news articles"""

    return News.query.all()


def save_news_article(user_id, news_id):
    """Save news articles to database"""

    saved_article = My_news(user_id=user_id, news_id=news_id)

    db.session.add(saved_article)
    db.session.commit()

    return saved_article


def get_saved_news_by_id(user_id):
    """Find launch that has been saved by session user"""

    return My_news.query.filter(My_news.user_id == user_id).all()


def delete_news_article(my_news_id, news_title):
    """Remove user's saved news article from database"""

    delete_article = My_news.query.get(my_news_id)

    db.session.delete(delete_article)
    db.session.commit()

    return news_title


# TODO
# def pretty_time():
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
