#!/usr/bin/python3

"""a function that queries the Reddit API and returns the number of
subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-agent": "linux:0x016.api.advanced:v1.0.0"
            }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
