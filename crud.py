"""CRUD operations"""


# from model import db, User, UpcomingLaunch, myLaunch, connect_to_db
# from api import upcoming_launch_api


#######################################
#                                     #
#                                     #
#               USERS                 #
#                                     #
#                                     #
#######################################


# def create_user(fname, lname, email, password, mobile_number):

#     # create a user
#     user = User(fname=fname, lname=lname, email=email,
#                 password=password, mobile_number=mobile_number)

#     # add user to database
#     db.session.add(user)
#     db.session.commit()

#     return user


#######################################
#                                     #
#                                     #
#              Launches               #
#                                     #
#                                     #
#######################################


# def create_upcoming_launch(launch_api_id, name, status_name, window_start, mission_description, pad_location, image):

#     # create a launch
#     upcoming_launch = UpcomingLaunch(launch_api_id=launch_api_id, name=name, status_name=status_name,
#                                      window_start=window_start, mission_description=mission_description, pad_loaction=pad_location, image=image)

#     # save launch to database
#     db.session.add(upcoming_launch)
#     db.session.commit()

#     return upcoming_launch


# def seed_database(data):??


# def save_launch()


# def countdown_timer(pass_in_start_window):
#     """create coundown from start window"""
#     return countdown
