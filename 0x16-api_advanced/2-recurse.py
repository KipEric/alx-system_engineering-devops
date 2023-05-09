#!/usr/bin/python3
""" A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that queries the reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API Client"}

    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if "data" not in data or "children" not in data["data"]:
            return hot_list

        posts = data["data"]["children"]

        if len(posts) == 0:
            return hot_list

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
    else:
        return None
