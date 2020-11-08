import requests
import json


def upcoming_launch_api():
    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json")

    # data needs to be used in server route and to seed database?
    data = res.json()['results']

    # for launch in data:

    #     (launch['name'])
    #     (launch['status']['name'])
    #     (launch['window_start'])
    #     (launch['mission']['description'])
    #     (launch['pad']['location']['name'])
    #     (launch['image'])

    return data
