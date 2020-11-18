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

    ########################
    # print(news_data[0]['title'])
    # print(news_data)

    # return(news_data)

    # for dic in news_data:
    #     for key in dic:
    #         print(dic[key])

    for dic in news_data:
        title, url, image, news_site, summary, date = (
            dic['title'], dic['url'], dic['imageUrl'], dic['newsSite'], dic['summary'], dic['publishedAt'])

        print(title, url, image, news_site, summary, date)
