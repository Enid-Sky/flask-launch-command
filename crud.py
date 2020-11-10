"""CRUD operations"""


from model import db, User, Upcominglaunch, Mylaunch, connect_to_db
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


#######################################
#                                     #
#                                     #
#              Launches               #
#                                     #
#                                     #
#######################################


def create_upcoming_launch(name, status_name, window_start, mission_description, pad_location, image):

    # create a launch
    upcoming_launch = Upcominglaunch(name=name, status_name=status_name,
                                     window_start=window_start, mission_description=mission_description, pad_location=pad_location, image=image)

    # save launch to database
    db.session.add(upcoming_launch)
    db.session.commit()

    print('::create upcoming launch::')

    return upcoming_launch


# STILL NEEDS TESTING
def my_launch_to_db(user_id, launch_id):
    """Creates a saved launch by user"""

    saved = Mylaunch(user_id=user_id, launch_id=launch_id)

    db.session.add(saved)
    db.session.commit()

    return saved


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
