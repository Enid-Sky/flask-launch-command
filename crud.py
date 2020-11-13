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


def my_launch_to_db(user_id, launch_id):
    """Create and return launch that has been saved by session user"""

    saved_launch = Mylaunch(user_id=user_id, launch_id=launch_id)

    db.session.add(saved_launch)
    db.session.commit()

    return saved_launch


def delete_my_launch(launch_id, user_id):
    """Remove a user's saved launch from the database"""

    delete_launch = Mylaunch.query.filter(
        Mylaunch.launch_id == launch_id, Mylaunch.user_id == user_id).first()
    # delete_launch = Mylaunch.query.filter(launch_id)

    # delete_launch = Mylaunch.query.filter(myLaunch.launch_id == launch_id).first()

    # delete_launch = Mylaunch(user_id=user_id, launch_id=launch_id)

    # delete_launch = Mylaunch.query.filter(Mylaunch.launch_id=launch_id, Mylaunch.user_id=user_id).first()

    db.session.delete(delete_launch)
    db.session.commit()

    return delete_launch


# def delete_my_launch_from_db(user_id):


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


# TODO
# def pretty_time():


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
