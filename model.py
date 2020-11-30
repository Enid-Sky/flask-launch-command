"""Models for launch command app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


db = SQLAlchemy()


class User(db.Model):
    """User details"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        unique=True,
                        autoincrement=True)

    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False, unique=True)

    # my_launches = a list of MyLaunch objects

    def __repr__(self):
        """Show info about user"""

        return f"<User info: id = {self.user_id}, name = {self.fname} {self.lname} email = {self.email}>"


class Upcominglaunch(db.Model):
    """Upcoming launch details"""

    __tablename__ = "launches"

    upcomingLaunch_id = db.Column(db.Integer,
                                  primary_key=True,
                                  unique=True,
                                  autoincrement=True)

    # represent keys from API Data
    name = db.Column(db.String(100), nullable=False)
    status_name = db.Column(db.String(100), nullable=False)
    window_start = db.Column(db.DateTime(100), nullable=False)
    wiki_url = db.Column(db.String(1000), nullable=False)
    pad_location = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        """Show name of upcoming launch"""
        return f"{self.name} {self.status_name} {self.window_start} {self.wiki_url} {self.pad_location} {self.image}"


class Mylaunch(db.Model):
    """Launch saved by user"""

    __tablename__ = "my_launches"

    my_launch_id = db.Column(db.Integer,
                             primary_key=True,
                             autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    launch_id = db.Column(db.Integer, db.ForeignKey(
        'launches.upcomingLaunch_id'), nullable=False)

    # relationship references
    launch = db.relationship('Upcominglaunch', backref='Mylaunch')
    user = db.relationship('User', backref='Mylaunch')

    def __repr__(self):
        """Show info about user"""

        return f"<Upcoming launch details: id = {self.my_launch_id}, user = {self.user_id} launch_id = {self.launch_id}>"

#######################################
#                                     #
#                                     #
#            News Articles            #
#                                     #
#                                     #
#######################################


class News(db.Model):
    """Creates news articles"""

    __tablename__ = "news_articles"

    news_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)

    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    news_site = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.DateTime(50), nullable=False)

    def __repr__(self):
        """Show info about news """

        return f"<News: id = {self.news_id}, title = {self.title} summary = {self.summary}>"


class My_news(db.Model):
    """News saved by user"""

    __tablename__ = "my_news_articles"

    my_news_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)

    news_id = db.Column(db.Integer, db.ForeignKey(
        'news_articles.news_id'), nullable=False)

    # relationship references
    news_user = db.relationship('User', backref='My_news')
    news_article = db.relationship('News', backref='My_news')

    def __repr__(self):
        """Show info about news """

        return f"<News: id = {self.news_id} >"


#######################################
#                                     #
#                                     #
#            Messaging                #
#                                     #
#                                     #
#######################################

class Messaging(db.Model):
    """Return messaging info"""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    launch_id = db.Column(db.Integer, db.ForeignKey(
        'launches.upcomingLaunch_id'), nullable=False)

# NOTE: might need to add column for message content and dates?

# NOTE: might need to refer to my launches instead of upcoming launches instead

    # relationship references
    launch = db.relationship('Upcominglaunch', backref='Messaging')
    user = db.relationship('User', backref='Messaging')

    def __repr__(self):
        """Show name of upcoming launch"""
        return f"Message_id:{self.message_id}, user id: {self.status_name}, launch id: {self.launch_id}, launch name: {self.launch_id.launch.name}"


##############################################################################


def connect_to_db(flask_app, db_uri='postgresql:///launchcommand', echo=True):
    """Connect the database to the Flask app"""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
