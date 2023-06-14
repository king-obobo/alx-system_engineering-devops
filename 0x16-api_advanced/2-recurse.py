#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
The list contains the titles of all hot articles for a given subreddit.
Returns None if no reslts are found
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }
    params = {
        "after": after
    }

    res = requests.get(URL, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        for all_data in res.json().get("data").get("children"):
            new_data = all_data.get("data")
            title = new_data.get("title")
            hot_list.append(title)
        after = res.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
