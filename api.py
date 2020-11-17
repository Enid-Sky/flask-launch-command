import requests
import json


def upcoming_launch_api():
    res = requests.get(
        "https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json")

    data = res.json()['results']

    return data


def news_api():
    news_res = requests.get(
        "https://test.spaceflightnewsapi.net/api/v2/articles?_limit=10")

    news_data = news_res.json()

    return(news_data)

    ########################
    # print(news_data[0]['title'])
