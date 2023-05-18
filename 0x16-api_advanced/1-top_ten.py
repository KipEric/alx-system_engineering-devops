#!/usr/bin/python3
"""function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """A Function that prints all the title of 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API Client"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
