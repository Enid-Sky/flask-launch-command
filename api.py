import requests
import json


def upcoming_launch_api():
    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?format=json&limit=10&offset=3")

    data = res.json()['results']

    return data
