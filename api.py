import requests
import json


def upcoming_launch_api():
    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json")

    data = res.json()['results']
    return data
