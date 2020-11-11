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

        return f"<User info: id = {self.user_id}, name = {self.fname} {self.lname}>"


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
    image = db.Column(db.String(1000), nullable=False)

    # my_launches = a list of MyLaunch objects

    def __repr__(self):
        """Show name of upcoming launch"""
        return f"<Upcoming launch name: {self.name}>"


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
        """Show infor about user"""

        return f"<Upcoming launch details: id = {self.my_launch_id}, user = {self.user_id} launch_id = {self.upcomingLaunch_id}>"


#####################################################################
# FEATURE MODELS

# class News(db.Model):
#     """Latest spaceflight news"""


# class MyNews(db.Model):
#     """News article saved by user"""


# class TwilioMessage(db.Model):
#     """Launch reminder message"""


##############################################################################
# DATABASE FUNCTIONS

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
