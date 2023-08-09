#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:oxo16.api.advanced:v1.0.0"
            }
    params = {
            "limit": 10
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
