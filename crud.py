"""CRUD operations"""


from model import db, User, UpcomingLaunch, myLaunch, connect_to_db


def create_user(fname, lname, email, password, mobile_number):

    # create a user
    user = User(fname=fname, lname=lname, email=email,
                password=password, mobile_number=mobile_number)

    # add user to database
    db.session.add(user)
    db.session.commit()

    return user
