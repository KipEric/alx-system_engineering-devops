#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """A Function that returns number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit API Client"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
