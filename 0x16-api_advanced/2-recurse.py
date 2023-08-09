#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit. Returns None if no results"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:oxo16.api.advanced:v1.0.0"
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
