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

    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False, unique=True)

    # relationship
    my_launch = db.relationship('myLaunch')

    def __repr__(self):
        """Show infor about user"""

        return f"<User info: id = {self.user_id}, name = {self.fname} {self.lname}>"


class UpcomingLaunch(db.Model):
    """Upcoming launch details"""

    __tablename__ = "launches"

    upcomingLaunch_id = db.Column(db.Integer,
                                  primary_key=True,
                                  unique=True,
                                  autoincrement=True)

    launch_api_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=False)
    status_name = db.Column(db.String, nullable=False)
    window_start = db.Column(db.DateTime, nullable=False)
    mission_description = db.Column(db.String(200), nullable=False)
    pad_location = db.Column(db.String, nullable=False)
    image = db.Column(db.String(10000), nullable=False)

    # relationship
    my_launch = db.relationship('myLaunch')

    def __repr__(self):
        """Show infor about user"""

        return f"<Upcoming launch details: id = {self.upcomingLaunch_id}, name = {self.name}>"


class myLaunch(db.Model):
    """Launch saved by user"""

    __tablename__ = "my_launches"

    my_launch_id = db.Column(db.Integer,
                             primary_key=True,
                             unique=True,
                             autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    launch_id = db.Column(db.Integer, db.ForeignKey(
        'launches.upcomingLaunch_id'), nullable=False)

    # relationships
    user = db.relationship('User')
    launch = db.relationship('UpcomingLaunch')

    def __repr__(self):
        """Show infor about user"""

        return f"<Upcoming launch details: id = {self.my_launch_id}, user = {self.user_id}>"


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
