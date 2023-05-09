#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
parses the title of all hot articles.
"""


import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """ A recursive function that queries the Reddit API"""
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API Client"}

    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if after is None:
            sorted_counts = sorted(
                    count_dict.items(),
                    key=lambda x: (-x[1], x[0].lower())
            )
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
            return

        for post in posts:
            title = post["data"]["title"]
            words = title.lower().split()

            for word in word_list:
                word = word.lower()
                for w in words:
                    if word == w and not any(ch.isalpha() for ch in word):
                        count_dict[word] = count_dict.get(word, 0) + 1

        after = data["data"]["after"]
        count_words(subreddit, word_list, after=after, count_dict=count_dict)
    else:
        return
